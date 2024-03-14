from haystack import Pipeline
from haystack_integrations.document_stores.elasticsearch import ElasticsearchDocumentStore
from haystack_integrations.components.retrievers.elasticsearch import ElasticsearchEmbeddingRetriever
from haystack.components.embedders import OpenAITextEmbedder
from haystack.components.builders import DynamicPromptBuilder
from haystack.components.generators import OpenAIGenerator

class HaystackPipelineFactory():
    def create_retriever_pipeline(self, top_k: int) -> Pipeline:
        document_store = ElasticsearchDocumentStore(hosts = "http://elasticsearch:9200")
        embedder = OpenAITextEmbedder()
        retriever = ElasticsearchEmbeddingRetriever(document_store=document_store, top_k=top_k)
        pipeline = Pipeline()
        pipeline.add_component("embedder", embedder)
        pipeline.add_component("retriever", retriever)
        pipeline.connect("embedder.embedding", "retriever.query_embedding")
        return pipeline

    def create_query_with_document_pipeline(self,) -> Pipeline:
        prompt_builder = DynamicPromptBuilder(runtime_variables=["documents"])
        llm = OpenAIGenerator()
        pipeline = Pipeline()
        pipeline.add_component("prompt_builder", prompt_builder)
        pipeline.add_component("llm", llm)
        pipeline.connect("prompt_builder", "llm")
        return pipeline
    
    def create_query_pipeline(self,) -> Pipeline:
        prompt_builder = DynamicPromptBuilder()
        llm = OpenAIGenerator()
        pipeline = Pipeline()
        pipeline.add_component("prompt_builder", prompt_builder)
        pipeline.add_component("llm", llm)
        pipeline.connect("prompt_builder", "llm")
        return pipeline