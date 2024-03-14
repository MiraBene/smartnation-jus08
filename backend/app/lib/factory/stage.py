from lib.stage import (ValidateLanguageStage,
                       ValidateQualityStage,
                       RAGStage,
                       RetryCounterStage,
                       RetrieveStage)
from haystack import Pipeline

class StageFactory():
    def create_retriever_stage(self, uuid: str, pipeline: Pipeline):
        return RetrieveStage(uuid, pipeline)
        
    def create_val_quality_stage(self, uuid: str, pipeline: Pipeline):
        return ValidateQualityStage(uuid=uuid, pipeline=pipeline)

    def create_val_language_stage(self, uuid: str, pipeline: Pipeline):
        return ValidateLanguageStage(uuid=uuid, pipeline=pipeline)

    def create_rag_stage(self, uuid: str, pipeline: Pipeline):
        return RAGStage(uuid=uuid, pipeline=pipeline)

    def create_retry_stage(self, uuid: str, n_retry: int):
        return RetryCounterStage(uuid=uuid, n_retry=n_retry)
