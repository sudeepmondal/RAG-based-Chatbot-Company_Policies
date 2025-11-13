import os
import re
from typing import List, Dict
from PyPDF2 import PdfReader

class DocumentProcessor:
    """Process and chunk documents for RAG"""
    
    def __init__(self, chunk_size: int = 500, chunk_overlap: int = 50):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
    
    def load_pdf(self, file_path: str) -> str:
        """Extract text from PDF file"""
        try:
            reader = PdfReader(file_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            return text
        except Exception as e:
            print(f"Error reading PDF {file_path}: {e}")
            return ""
    
    def load_text(self, file_path: str) -> str:
        """Load text from .txt file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"Error reading text file {file_path}: {e}")
            return ""
    
    def load_document(self, file_path: str) -> str:
        """Load document based on file extension"""
        ext = os.path.splitext(file_path)[1].lower()
        if ext == '.pdf':
            return self.load_pdf(file_path)
        elif ext == '.txt':
            return self.load_text(file_path)
        else:
            raise ValueError(f"Unsupported file type: {ext}")
    
    def clean_text(self, text: str) -> str:
        """Clean and normalize text"""
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        # Remove special characters but keep punctuation
        text = re.sub(r'[^\w\s.,!?-]', '', text)
        return text.strip()
    
    def chunk_text(self, text: str) -> List[str]:
        """Split text into chunks with overlap"""
        text = self.clean_text(text)
        words = text.split()
        chunks = []
        
        for i in range(0, len(words), self.chunk_size - self.chunk_overlap):
            chunk = ' '.join(words[i:i + self.chunk_size])
            if chunk:
                chunks.append(chunk)
        
        return chunks
    
    def process_documents(self, file_paths: List[str]) -> List[Dict]:
        """Process multiple documents and return chunks with metadata"""
        all_chunks = []
        
        for file_path in file_paths:
            try:
                text = self.load_document(file_path)
                chunks = self.chunk_text(text)
                
                for i, chunk in enumerate(chunks):
                    all_chunks.append({
                        'text': chunk,
                        'source': os.path.basename(file_path),
                        'chunk_id': i
                    })
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
        
        return all_chunks