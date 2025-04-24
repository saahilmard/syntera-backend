from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

def get_relevant_context(query):
    embeddings = OpenAIEmbeddings()
    vectordb = FAISS.load_local("rag_pipeline/medical_faiss_index", embeddings)
    results = vectordb.similarity_search(query, k=3)
    return "\n".join([r.page_content for r in results]) 