import os
import fitz  # PyMuPDF
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

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
    embeddings = OpenAIEmbeddings()
    vectordb = FAISS.from_documents(chunks, embeddings)
    vectordb.save_local("rag_pipeline/medical_faiss_index")

if __name__ == "__main__":
    pdf_folder = "rag_pipeline/rag_docs"
    chunks = load_pdf_text_chunks(pdf_folder)
    create_vector_store(chunks)
    print(f"Successfully processed PDFs and created vector store with {len(chunks)} chunks") 