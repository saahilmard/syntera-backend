import os
import fitz  # PyMuPDF
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

# Load environment variables from .env file
load_dotenv()

def load_pdf_text_chunks(pdf_folder: str):
    chunks = []
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

    for filename in os.listdir(pdf_folder):
        if filename.endswith(".pdf"):
            filepath = os.path.join(pdf_folder, filename)
            doc = fitz.open(filepath)
            full_text = ""
            for page in doc:
                full_text += page.get_text()
            docs = splitter.create_documents([full_text])
            chunks.extend(docs)
    return chunks

def create_vector_store(chunks):
    # Configure embeddings
    embeddings = OpenAIEmbeddings(
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )
    vectordb = FAISS.from_documents(chunks, embeddings)
    # Use absolute path for vector store
    current_dir = os.path.dirname(os.path.abspath(__file__))
    index_path = os.path.join(current_dir, "medical_faiss_index")
    vectordb.save_local(index_path)

if __name__ == "__main__":
    # Use absolute path for PDF folder
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_folder = os.path.join(current_dir, "rag_docs")
    chunks = load_pdf_text_chunks(pdf_folder)
    create_vector_store(chunks)
    print(f"Successfully processed PDFs and created vector store with {len(chunks)} chunks") 