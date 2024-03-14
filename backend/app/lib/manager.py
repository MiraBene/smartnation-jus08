from lib.orchestrator import PipelineOrchestrator
from lib.factory import StageFactory, HaystackPipelineFactory
from lib import const as C

class AnswerManager():
    def __init__(self):
        self.stage_factory = StageFactory()
        self.pipeline_factory = HaystackPipelineFactory()
    
    def build_orchestrator(self):
        pipeline_retriever = self.pipeline_factory.create_retriever_pipeline(C.TOP_K_RETRIEVER)
        pipeline_w_docs = self.pipeline_factory.create_query_with_document_pipeline()
        pipeline_wo_docs = self.pipeline_factory.create_query_pipeline()

        retriever = self.stage_factory.create_retriever_stage("retriever", pipeline_retriever)
        rag = self.stage_factory.create_rag_stage("rag", pipeline_w_docs)
        retry_ctr = self.stage_factory.create_retry_stage("retry", C.N_RETRY)
        val_lang = self.stage_factory.create_val_language_stage("validate language", pipeline_wo_docs)
        val_quality = self.stage_factory.create_val_quality_stage("validate quality", pipeline_w_docs)
        orchestrator = PipelineOrchestrator(retriever=retriever, 
                                            rag=rag, 
                                            val_language=val_lang, 
                                            val_quality=val_quality, 
                                            retry_ctr=retry_ctr)
        return orchestrator
        
