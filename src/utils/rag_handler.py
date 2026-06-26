import os
import shutil
from pypdf import PdfReader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

class DocRAGHandler:
    def __init__(self, db_dir: str = "./chroma_db"):
        self.db_dir = db_dir
        # CRITICAL FIX: Using the current 2026 Gemini embedding model
        self.embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
        self.vector_store = None

    def clear_existing_db(self):
        """Clears the local vector store directory to prevent context pollution."""
        if os.path.exists(self.db_dir):
            shutil.rmtree(self.db_dir)

    def extract_text_from_pdf(self, pdf_file) -> str:
        """Extracts plain text character streams from the uploaded PDF data asset."""
        reader = PdfReader(pdf_file)
        full_text = []
        for page_num, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                full_text.append(f"--- Page {page_num + 1} ---\n{text}")
        return "\n".join(full_text)

    def ingest_pdf(self, pdf_file) -> int:
        """Parses, chunks, embeds, and persists PDF data structures into ChromaDB."""
        self.clear_existing_db()
        
        raw_text = self.extract_text_from_pdf(pdf_file)
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=150,
            length_function=len,
            is_separator_regex=False,
        )
        
        chunks = text_splitter.split_text(raw_text)
        documents = [Document(page_content=chunk, metadata={"source": "uploaded_doc.pdf"}) for chunk in chunks]
        
        # Initialize and persist using native langchain-chroma wrapper
        self.vector_store = Chroma.from_documents(
            documents=documents,
            embedding=self.embeddings,
            persist_directory=self.db_dir
        )
        return len(documents)

    def query_knowledge_base(self, query: str, k: int = 4) -> str:
        """Retrieves matching structural context matching targeted update nodes."""
        if not self.vector_store:
            self.vector_store = Chroma(persist_directory=self.db_dir, embedding_function=self.embeddings)
            
        docs = self.vector_store.similarity_search(query, k=k)
        return "\n\n".join([f"[Source: {d.metadata.get('source')}]\n{d.page_content}" for d in docs])