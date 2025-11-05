import os

import chromadb

from nomic import embed
import nomic


client = chromadb.CloudClient(
  api_key=os.environ.get("CHROMA_API_KEY"),
  tenant='32d78b6f-1a11-4ac5-90c3-69baa6c7b763',
  database='huma'
)

nomic.login(os.environ.get("ATLAS_NOMIC"))
def get_collection(chat_id: int):
    return client.get_or_create_collection(
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