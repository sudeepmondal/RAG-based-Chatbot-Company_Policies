# RAG-based-Chatbot (Company-Policies)

# 📚 RAG Company Policy Chatbot

A production-ready Retrieval-Augmented Generation (RAG) chatbot that answers questions about company policies using semantic search and AI-powered responses.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🌟 Features

- ✅ **PDF & Text Document Support** - Ingest company policies in multiple formats
- ✅ **Semantic Search** - Uses SentenceTransformers embeddings + FAISS vector store
- ✅ **AI-Powered Responses** - Groq (FREE) or OpenAI integration
- ✅ **Source Citations** - Shows which documents were used to generate answers
- ✅ **Conversation Memory** - Maintains context across multiple questions
- ✅ **Real-time Document Upload** - Add new policies without restarting
- ✅ **Beautiful UI** - Clean, intuitive Streamlit interface
- ✅ **Multi-Provider Support** - Free mode, Groq, or OpenAI

## 🎥 Demo

![Demo Screenshot](docs/screenshot.png)

**Example Queries:**
- "What is the company's leave policy?"
- "How can employees request remote work?"
- "What are the password requirements?"

## 🏗️ Architecture

```
User Query
    ↓
[1] Document Processing (PyPDF2)
    ↓
[2] Text Chunking (500 tokens with 50 overlap)
    ↓
[3] Embedding Generation (SentenceTransformers)
    ↓
[4] Vector Storage (FAISS)
    ↓
[5] Semantic Search (Cosine Similarity)
    ↓
[6] Context Retrieval (Top-3 chunks)
    ↓
[7] LLM Generation (Groq Llama 3.3)
    ↓
[8] Response + Citations
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager
- (Optional) Groq API key for AI responses

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/rag-company-chatbot.git
cd rag-company-chatbot
```

2. **Create virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables** (Optional)
```bash
# Create .env file
echo "GROQ_API_KEY=your_key_here" > .env
```

5. **Add sample documents**
```bash
# Create data folder and add your policy documents
mkdir data
# Add your .txt or .pdf files to data/
```

6. **Run the application**
```bash
streamlit run app.py
```

7. **Open in browser**
```
http://localhost:8501
```

## 📁 Project Structure

```
rag-company-chatbot/
├── app.py                     # Streamlit UI & main application
├── rag_engine.py              # RAG core logic (embeddings, retrieval, generation)
├── document_processor.py      # PDF/Text processing & chunking
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (API keys)
├── .gitignore                # Git ignore file
├── data/                      # Company policy documents
│   ├── leave_policy.txt
│   ├── remote_work_policy.txt
│   └── it_security_policy.txt
└── README.md                  # This file
```

## 🔑 Getting API Keys

### Groq (Recommended - FREE!)

1. Visit: https://console.groq.com
2. Sign up with Google or email
3. Navigate to API Keys section
4. Create new API key
5. Copy and add to `.env` file

**Free Tier Limits:**
- 14,400 requests/day
- 30 requests/minute
- Unlimited tokens

### OpenAI (Optional)

1. Visit: https://platform.openai.com
2. Create account
3. Add payment method
4. Generate API key
5. Add to `.env` file

## 🎯 Usage

### Basic Usage

1. **Select API Provider**
   - Free Mode (rule-based responses)
   - Groq (AI-powered, FREE)
   - OpenAI (AI-powered, paid)

2. **Upload Documents**
   - Click "Upload Documents" in sidebar
   - Select PDF or TXT files
   - Click "Initialize RAG System"

3. **Ask Questions**
   - Type your question in chat box
   - Press Enter or click Send
   - View AI response with source citations

### Sample Questions

```
"What is the leave policy?"
"How many sick days do I get?"
"How can I request remote work?"
"What are the password requirements?"
"Tell me about parental leave"
"What equipment is provided for remote work?"
```

### Conversation Memory

The chatbot remembers your conversation context:

```
You: "What is the leave policy?"
Bot: [Explains leave policy]

You: "How many sick days?"
Bot: [Understands context, answers about sick leave]

You: "Can I carry them over?"
Bot: [Knows "them" = sick days, provides specific answer]
```

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **LLM** | Groq (Llama 3.3-70B) | Text generation |
| **Embeddings** | SentenceTransformers | Semantic search |
| **Vector Store** | FAISS | Efficient similarity search |
| **Backend** | Python 3.8+ | Core logic |
| **Frontend** | Streamlit | User interface |
| **PDF Processing** | PyPDF2 | Document parsing |

## ⚙️ Configuration

### Customizing Chunk Size

Edit `document_processor.py`:

```python
processor = DocumentProcessor(
    chunk_size=500,      # Tokens per chunk
    chunk_overlap=50     # Overlap between chunks
)
```

### Changing Embedding Model

Edit `rag_engine.py`:

```python
RAGEngine(
    model_name="all-MiniLM-L6-v2"  # Fast, good quality
    # model_name="all-mpnet-base-v2"  # Slower, better quality
)
```

### Adjusting Retrieval

Edit `app.py`:

```python
result = st.session_state.rag_engine.query(
    prompt,
    top_k=3,  # Number of chunks to retrieve
    conversation_history=history
)
```

## 🐛 Troubleshooting

### Common Issues

**1. ModuleNotFoundError: No module named 'streamlit'**
```bash
# Ensure virtual environment is activated
venv\Scripts\activate
pip install -r requirements.txt
```

**2. FAISS installation error**
```bash
pip install faiss-cpu --no-cache-dir
```

**3. API Error: Model decommissioned**
```python
# Update model name in rag_engine.py
self.model = "llama-3.3-70b-versatile"
```

**4. PowerShell execution policy error**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## 📊 Performance

- **Document Processing:** ~1-2 seconds per document
- **Embedding Generation:** ~0.5 seconds per query
- **Vector Search:** <0.1 seconds
- **LLM Response:** 1-3 seconds (Groq), 3-5 seconds (OpenAI)
- **Total Response Time:** ~2-5 seconds

## 🔒 Security

- API keys stored in `.env` (not committed to Git)
- No data stored externally
- All processing happens locally
- Session-based conversation memory

## 🚢 Deployment

### Streamlit Cloud (FREE)

1. Push to GitHub
2. Visit: https://streamlit.io/cloud
3. Connect repository
4. Add secrets (API keys)
5. Deploy!

### Docker (Optional)

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "app.py"]
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing UI framework
- [Groq](https://groq.com/) for free, fast LLM inference
- [Sentence Transformers](https://www.sbert.net/) for embeddings
- [FAISS](https://github.com/facebookresearch/faiss) for vector search
- [OpenAI](https://openai.com/) for pioneering LLM technology

## 📚 Resources

- [RAG Overview](https://aws.amazon.com/what-is/retrieval-augmented-generation/)
- [Groq Documentation](https://console.groq.com/docs)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [FAISS Tutorial](https://github.com/facebookresearch/faiss/wiki)

## 🗺️ Roadmap

- [ ] Add support for DOCX files
- [ ] Implement multi-language support
- [ ] Add conversation export feature
- [ ] Create REST API endpoints
- [ ] Add authentication system
- [ ] Implement analytics dashboard
- [ ] Support for multiple vector stores (Chroma, Pinecone)

## ⭐ Star History

If you find this project helpful, please consider giving it a star!

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/rag-company-chatbot&type=Date)](https://star-history.com/#yourusername/rag-company-chatbot&Date)

---

**Made with ❤️ using Python, Streamlit, and AI**
