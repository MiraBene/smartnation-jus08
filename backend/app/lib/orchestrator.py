from __future__ import annotations

from .stage import (RAGStage, RetrieveStage,
                    ValidateLanguageStage,
                    ValidateQualityStage,
                    RetryCounterStage)
from lib import const as C

class PipelineOrchestrator:
    def __init__(self, retriever: RetrieveStage,
                       rag: RAGStage,
                       val_language: ValidateLanguageStage,
                       val_quality: ValidateQualityStage,
                       retry_ctr: RetryCounterStage) -> None:

        self._is_finished = False
        self._is_dropped = False

        self.retriever = retriever
        self.rag = rag
        self.retry_ctr = retry_ctr
        self.val_language = val_language
        self.val_quality = val_quality
    @property
    def result(self):
        if self.is_success():
            return self.rag.data
        else:
            return None
    
    def run(self, question: str):
        self.retriever.run(question=question)
        docs = self.retriever.data

        while not self._is_finished and not self._is_dropped:
            self.rag.run(template=C.BASE_TEMPLATE_RAG,
                         question=question,
                         documents=docs)

            self.retry_ctr.run()
            print(self.retry_ctr.n_retry)

            if not self.rag.did_succeed():
                self.rag.reset()
                if self.retry_ctr.n_retry == 0:
                    self._is_dropped = True
                continue

            self.val_language.run(question=question,
                                  answer=self.rag.data)
            if not self.val_language.did_succeed():
                self.rag.reset() # possibly enforce new prompt
                self.val_language.reset()
                continue

            self.val_quality.run(answer=self.rag.data,
                                 question=question,
                                 documents=docs)
            if not self.val_quality.did_succeed():
                self.rag.reset() # possibly enforce new prompt
                self.val_language.reset()
                self.val_quality.reset()
            self._is_finished = True

    def is_success(self):
        return self._is_finished and not self._is_dropped
