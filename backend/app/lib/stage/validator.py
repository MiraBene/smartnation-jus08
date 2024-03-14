from lib.stage.base import BaseStage
from haystack import Pipeline
from lib import const as C

import json
from pydantic import BaseModel
from typing import Literal, List
from pydantic import ValidationError
from haystack.dataclasses import Document

class DataValidateLanguage(BaseModel):
    question: str
    answer: str
    same_language: Literal['yes', 'no']

class DataRulesLanguage(BaseModel):
    rules_followed: Literal['yes', 'no']
    reason: str
    
class ValidateLanguageStage(BaseStage):
    def __init__(self, uuid: str, 
                 pipeline: Pipeline):
        BaseStage.__init__(self, uuid)
        self.pipeline = pipeline
        self.data: DataValidateLanguage|None
    
    def validate_output(self, json_str: str) -> bool:
        obj = None
        try:
            # Attempt to parse the string into JSON
            data = json.loads(json_str)
            # Validate the parsed JSON data against the Pydantic model
            obj = DataValidateLanguage(**data)
            return True, obj
        except (ValidationError, json.JSONDecodeError):
            # If a ValidationError is raised by Pydantic or
            # a JSONDecodeError is raised by json.loads(), return False
            return False, None

    def action(self,question: str,
                    answer: str,
                    template: str=None):
        if template is None:
            template = C.TEMPLATE_VAL_LANGUAGE
        data = {"prompt_builder": {
                                    "prompt_source": template,
                                    "template_variables": {"question": question,
                                                        "answer": answer},
                                    },
        }
        results = self.pipeline.run(data)
        output = results['llm']['replies'][0]

        success, obj = self.validate_output(output)
        self.success = success
        self.data = obj

class ValidateQualityStage(BaseStage):
    def __init__(self, uuid: str, pipeline: Pipeline):
        BaseStage.__init__(self, uuid)
        self.pipeline = pipeline

    def validate_output(self, json_str: str) -> bool:
        obj = None
        try:
            # Attempt to parse the string into JSON
            data = json.loads(json_str)
            # Validate the parsed JSON data against the Pydantic model
            obj = DataRulesLanguage(**data)
            return True, obj
        except (ValidationError, json.JSONDecodeError):
            # If a ValidationError is raised by Pydantic or
            # a JSONDecodeError is raised by json.loads(), return False
            return False, None

    def action(self, question: str, 
                     answer:str,
                     documents: List[Document],
                     template: str=None):
        if template is None:
            template = C.TEMPLATE_VAL_RULES
        data = {"prompt_builder": {
                                    "prompt_source": template,
                                    "template_variables": {"question": question,
                                                           "answer": answer},
                                    "documents": documents
                                    },
        }
        results = self.pipeline.run(data)
        output = results['llm']['replies'][0]
        success, obj = self.validate_output(output)
        self.success = success
        self.data = obj