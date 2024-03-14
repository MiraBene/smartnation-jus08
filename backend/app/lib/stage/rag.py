from lib.stage.base import BaseStage
import haystack
from typing import List
from haystack.dataclasses import Document

class RetrieveStage(BaseStage):
    def __init__(self, uuid: str, pipeline: haystack.Pipeline ):
        BaseStage.__init__(self, uuid)
        self.pipeline = pipeline

    def action(self, question: str):
        data = {"embedder": {"text": question},}
        results = self.pipeline.run(data)
        self.data = results['retriever']['documents']
        self.success = True

class RAGStage(BaseStage):
    def __init__(self, uuid: str, pipeline: haystack.Pipeline ):
        BaseStage.__init__(self, uuid)
        self.pipeline = pipeline

    def action(self, template: str, question: str, documents: List[Document]):
        data = {"prompt_builder": {
                                    "prompt_source": template,
                                    "template_variables": {"question": question},
                                    "documents": documents
                                    },
        }
        results = self.pipeline.run(data)
        self.success = True
        self.data = results['llm']['replies'][0]
