import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

# Load environment variables from .env file
load_dotenv()

def get_relevant_context(query):
    # Configure embeddings
    embeddings = OpenAIEmbeddings(
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )
    current_dir = os.path.dirname(os.path.abspath(__file__))
    index_path = os.path.join(current_dir, "medical_faiss_index")
    vectordb = FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)
    results = vectordb.similarity_search(query, k=3)
    return "\n".join([r.page_content for r in results]) 