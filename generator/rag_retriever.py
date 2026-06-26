from generator.embedder import get_vector_store

def retrieve(feature_description: str, n_results: int = 3) -> list[str]:
    """
    Finds the n most semantically similar test case examples thi the given feature description
    
    Flow:
    1. get_vector_store() connects to ChromaDB with the local embedder
    2. similarity_search() embeds the query using the same model used at ingest time
    the finds the nearest vectors in the collection
    3. Each result is a langChain document - we return only raw text (page_content)
    
    n_results = 3 is the default - enough context for tghe LLM without bloatting the prompt
    Can be overridden if needed (e.g. for richer prompts on complex features)"""

    store = get_vector_store()
    results = store.similarity_search(feature_description, k=n_results)
    return [doc.page_content for doc in results]

