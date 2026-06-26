from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv
import os

load_dotenv()

COLLECTION_NAME = "qa_examples"

def get_embeddings():
    """
    Loads the all-MiniLM-L6-v2 model locally via sentence-transformers.

    This runs entirely on your machine — no API key, no cost, no rate limits.
    First call downloads ~90MB to ~/.cache/huggingface/ and caches it.
    Every subsequent call loads from cache instantly.
    """
    return HuggingFaceEmbeddings(model_name = "all-MiniLM-L6-v2")

def get_vector_store(persist_dir: str = None):
    """
    Returns a ChromaDB vector store backed by our local embeddings.

    ChromaDB stores vectors on disk (./chroma_db) so the knowledge base
    persists between runs — you only need to ingest once.

    persist_dir can be overridden for tests (we'll pass ':memory:' equivalent
    by using a temp dir so tests don't pollute the real DB).
    """

    persist_dir = persist_dir or os.getenv("CHROMA_PERSIST_DIR", "./chroma_db")
    embeddings = get_embeddings()
    return Chroma(
        collection_name = COLLECTION_NAME,
        embedding_function = embeddings,
        persist_directory = persist_dir
    )