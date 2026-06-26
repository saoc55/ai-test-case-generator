import sys
from pathlib import Path

#Adds the ürpject root to Python's module search path
# Needed bause this script llives in a subdirectory (knowledge_Base/)
#but needs to import from generator/ which is a toot level

sys.path.insert(0, str(Path(__file__).parent.parent))

from generator.embedder import get_vector_store

SEED_DIR = Path(__file__).parent/ "seed_data"

def load_chunks():
    """
    Reads all .md files in seed_data/ and splits them into 
    individual testcase chunks using ## headers as delimiters

    Returns two parallel lists:
    - chunks: the raw text of each case
    - metada: dict per chunk with source filename and position index
    (stored in ChromaDB alongside the vecor for filtering/debugging)
    """

    chunks = []
    metadatas = []

    for md_file in SEED_DIR.glob("*.md"):
        content = md_file.read_text(encoding="utf-8")

        #Split on ## each test case starts with ## TC-XXX-NNN
        #sections[0] is the file title (# header), skip it
        sections = content.split("\n##")

        for i, section in enumerate(sections[1:], start = 1):
            section = ("## " + section).strip() 
            if section:
                chunks.append(section)
                metadatas.append({"source": md_file.name, "chunk_index": i})

    return chunks, metadatas

def ingest():
    print("loading seed data...")
    chunks, metadatas = load_chunks()
    print (f"  Found {len(chunks)} test case chunks across {len(list(SEED_DIR.glob('*.md')))}files")
    store = get_vector_store()

    #Guard against double-ingestion -- ChromaDB will error oon duplicate IDS.
    #if the collection already has data, tell the user to wipe chroma_db/ and re-run

    existing = store._collection.count()
    if existing > 0:
        print(f"   ChromaDB already contains {existing} chunks. Nothing to do")
        print("    To re-ingest: delete the chroma_db/ folder and run this script agaian")
        return
    
    print("Embedding and storing chunks (first run downloads the model ~90MB)")
    store.add_texts(texts = chunks, metadatas = metadatas)

    print(f"Done. {len(chunks)} chunks ingested into ChromaDB")

if __name__ == "__main__":
    ingest()
