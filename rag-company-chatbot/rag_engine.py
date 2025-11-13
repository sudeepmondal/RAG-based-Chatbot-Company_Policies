import numpy as np
import faiss
from typing import List, Dict, Optional
from sentence_transformers import SentenceTransformer
from openai import OpenAI
import os

class RAGEngine:
    """RAG engine with embeddings, vector store, and generation"""
    
    def __init__(self, 
                 model_name: str = "all-MiniLM-L6-v2",
                 openai_api_key: Optional[str] = None,
                 groq_api_key: Optional[str] = None):
        """
        Initialize RAG engine
        
        Args:
            model_name: SentenceTransformer model for embeddings
            openai_api_key: OpenAI API key for generation
            groq_api_key: Groq API key for generation (FREE!)
        """
        print("Loading embedding model...")
        # Load embedding model
        self.embedding_model = SentenceTransformer(model_name)
        self.embedding_dim = self.embedding_model.get_sentence_embedding_dimension()
        
        # Initialize FAISS index
        self.index = faiss.IndexFlatL2(self.embedding_dim)
        self.documents = []
        
        # LLM client (prioritize Groq > OpenAI > None)
        if groq_api_key:
            self.client = OpenAI(
                api_key=groq_api_key,
                base_url="https://api.groq.com/openai/v1"
            )
            # Updated model names (as of 2025)
            self.model = "llama-3.3-70b-versatile"  # Latest stable model
            print(f"✅ Using Groq API with model: {self.model}")
        elif openai_api_key:
            self.client = OpenAI(api_key=openai_api_key)
            self.model = "gpt-3.5-turbo"
            print("✅ Using OpenAI API")
        else:
            self.client = None
            self.model = None
            print("ℹ️ Running in free mode (rule-based responses)")
    
    def create_embeddings(self, texts: List[str]) -> np.ndarray:
        """Create embeddings for texts"""
        embeddings = self.embedding_model.encode(texts, show_progress_bar=True)
        return embeddings.astype('float32')
    
    def add_documents(self, documents: List[Dict]):
        """Add documents to vector store"""
        texts = [doc['text'] for doc in documents]
        embeddings = self.create_embeddings(texts)
        
        # Add to FAISS index
        self.index.add(embeddings)
        self.documents.extend(documents)
        
        print(f"✅ Added {len(documents)} documents to vector store")
    
    def retrieve(self, query: str, top_k: int = 3) -> List[Dict]:
        """Retrieve top-k most relevant documents"""
        query_embedding = self.create_embeddings([query])
        
        # Search in FAISS
        distances, indices = self.index.search(query_embedding, top_k)
        
        results = []
        for idx, distance in zip(indices[0], distances[0]):
            if idx < len(self.documents):
                doc = self.documents[idx].copy()
                doc['score'] = float(distance)
                results.append(doc)
        
        return results
    
    def generate_response(self, 
                         query: str, 
                         context_docs: List[Dict],
                         conversation_history: List[Dict] = None) -> str:
        """Generate response using OpenAI with retrieved context"""
        
        if not self.client:
            # Fallback: Enhanced rule-based response
            context_text = "\n\n".join([doc['text'] for doc in context_docs])
            sources = list(set([doc['source'] for doc in context_docs]))
            
            # Format response nicely
            response = f"**Based on company policy documents:** {', '.join(sources)}\n\n"
            response += f"{context_text}\n\n"
            response += f"*💡 Note: This is retrieved from the policy documents. For GPT-4 powered answers, add your OpenAI API key.*"
            return response
        
        # Prepare context
        context = "\n\n".join([
            f"[Source: {doc['source']}]\n{doc['text']}" 
            for doc in context_docs
        ])
        
        # Build messages
        messages = [
            {
                "role": "system",
                "content": """You are a helpful assistant that answers questions about company policies. 
                Use ONLY the information provided in the context to answer questions.
                If the answer is not in the context, say "I don't have information about that in the company policies."
                Always cite the source document when providing information."""
            }
        ]
        
        # Add conversation history if provided
        if conversation_history:
            messages.extend(conversation_history[-6:])  # Last 3 exchanges
            print(f"📝 Using {len(conversation_history[-6:])} messages from conversation history")
        
        # Add current query with context
        messages.append({
            "role": "user",
            "content": f"""Context from company policies:

{context}

Question: {query}

Please answer based on the context above and cite the source."""
        })
        
        try:
            print(f"🔄 Calling {self.model}...")
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.3,
                max_tokens=500
            )
            print(f"✅ Got response from {self.model}")
            return response.choices[0].message.content
        except Exception as e:
            # Fallback to rule-based if API fails
            print(f"❌ API Error: {str(e)}")
            context_text = "\n\n".join([doc['text'] for doc in context_docs])
            sources = list(set([doc['source'] for doc in context_docs]))
            return f"**Based on:** {', '.join(sources)}\n\n{context_text}\n\n*(⚠️ API Error: {str(e)[:200]})*"
    
    def query(self, 
             question: str, 
             top_k: int = 3,
             conversation_history: List[Dict] = None) -> Dict:
        """Complete RAG query: retrieve + generate"""
        
        # Retrieve relevant documents
        retrieved_docs = self.retrieve(question, top_k)
        
        # Generate response
        response = self.generate_response(
            question, 
            retrieved_docs,
            conversation_history
        )
        
        return {
            'answer': response,
            'sources': retrieved_docs,
            'query': question
        }