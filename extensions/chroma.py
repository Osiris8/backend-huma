import os
import chromadb

from nomic import embed
import nomic
chroma_client = chromadb.PersistentClient(path="./chroma_db")

nomic.login(os.environ.get("ATLAS_NOMIC"))
def get_collection(chat_id: int):
    return chroma_client.get_or_create_collection(
        name=f"chat_{chat_id}",
        metadata={"dimension": 768})


def embed_text(text: str, task_type="search_document"):
    output = embed.text(
        texts=[text],
        model="nomic-embed-text-v1.5",
        task_type=task_type,
        dimensionality=256 
    )
    return output["embeddings"][0]