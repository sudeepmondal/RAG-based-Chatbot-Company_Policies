# 🤖 RAG-based Company Policy Chatbot

> An intelligent chatbot that answers questions about company policies using Retrieval-Augmented Generation (RAG)

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![FAISS](https://img.shields.io/badge/FAISS-Vector_Store-00ADD8?style=flat)](https://github.com/facebookresearch/faiss)
[![Groq](https://img.shields.io/badge/Groq-LLM-orange?style=flat)](https://groq.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---


## 🎯 Overview

This project implements a **production-ready RAG (Retrieval-Augmented Generation) chatbot** that can answer questions about company policies by:

1. **Reading** PDF and text documents containing company policies
2. **Embedding** document chunks using semantic search
3. **Retrieving** the most relevant information using FAISS vector database
4. **Generating** natural, contextual responses using AI (Groq/OpenAI)
5. **Citing** source documents for transparency

Perfect for HR departments, IT support, or any organization needing automated policy assistance!

---

## ✨ Features

### Core Features
- 📄 **Multi-format Support** - PDF and TXT document ingestion
- 🔍 **Semantic Search** - Uses SentenceTransformers for intelligent retrieval
- 💾 **Vector Database** - FAISS for fast similarity search
- 🤖 **AI-Powered** - Groq (FREE) 
- 📚 **Source Citations** - Shows which documents were used
- 💬 **Conversation Memory** - Maintains context across questions

### Additional Features
- 🎨 **Beautiful UI** - Clean Streamlit interface
- 📊 **Conversation Stats** - Track questions and topics
- 💾 **Export Chat** - Download conversation history
- 🆓 **Free Mode** - Works without API keys (rule-based)
- 🔄 **Real-time Upload** - Add documents without restart
- 🎯 **Relevance Scoring** - See how relevant each source is

---

## 📥 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/rag-company-chatbot.git
cd rag-company-chatbot
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

This will install:
- streamlit (UI framework)
- groq (LLM API client)
- sentence-transformers (embeddings)
- faiss-cpu (vector database)
- pypdf2 (PDF processing)
- python-dotenv (environment variables)

---

## ⚙️ Setup & Configuration

### 1. Environment Variables (Optional)

Create a `.env` file in the project root:

```bash
# For AI-powered responses (optional)
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

**Note:** The chatbot works in free mode without API keys!

### 2. Add Policy Documents

Place your company policy documents in the `data/` folder:

```bash
data/
├── leave_policy.txt
├── remote_work_policy.txt
└── it_security_policy.txt
```

Supported formats: `.txt`, `.pdf`

### 3. Run the Application

```bash
streamlit run app.py
```

The app will open automatically at: `http://localhost:8501`

---

## 📖 Usage Guide

### Basic Workflow

**Step 1: Select API Provider**

In the sidebar, choose:
- **Free Mode** - Rule-based responses (no API key needed)
- **Groq (FREE!)** - AI-powered with free Groq API
- **OpenAI** - AI-powered with OpenAI API (paid)

**Step 2: Upload Documents**

1. Click **"Upload Documents"** in sidebar
2. Select PDF or TXT files from your computer
3. Click **"🚀 Initialize RAG System"**
4. Wait for processing (1-2 seconds per document)

**Step 3: Ask Questions**

Type your question in the chat box:
- "What is the leave policy?"
- "How can I request remote work?"
- "What are the password requirements?"

**Step 4: View Results**

- AI-generated answer appears
- Click **"📚 View Sources"** to see:
  - Source document names
  - Relevant text chunks
  - Relevance scores

### Advanced Features

**Conversation Memory**
The chatbot remembers your conversation:
```
You: "What is the leave policy?"
Bot: [Explains policy]

You: "How many sick days?"  
Bot: [Understands context, answers about sick leave]
```

**Export Chat History**
1. Click **"💾 Export Chat"** in sidebar
2. Click **"⬇️ Download Chat History"**
3. Get a text file with full conversation

**Conversation Stats**
Sidebar shows:
- Number of questions asked
- Number of bot responses
- Recent questions list

---

## 📁 Project Structure

```
rag-company-chatbot/
│
├── app.py                      # Main Streamlit application
│   ├── UI components
│   ├── File upload handling
│   ├── Chat interface
│   └── Export functionality
│
├── rag_engine.py               # RAG core logic
│   ├── Embedding generation
│   ├── FAISS vector store
│   ├── Retrieval logic
│   └── LLM integration
│
├── document_processor.py       # Document processing
│   ├── PDF/Text loading
│   ├── Text cleaning
│   ├── Chunking algorithm
│   └── Metadata handling
│
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (API keys)
├── .gitignore                 # Git ignore rules
├── README.md                   # This file
│
└── data/                       # Policy documents folder
    ├── leave_policy.txt
    ├── remote_work_policy.txt
    └── it_security_policy.txt
```

---

## 🔑 API Keys Setup

### Groq API (Recommended - FREE!)

**Why Groq?**
- ✅ Completely free
- ✅ 14,400 requests/day
- ✅ Fast inference
- ✅ High-quality responses

**Setup Steps:**

1. Visit: https://console.groq.com
2. Sign up (free account)
3. Go to **API Keys** section
4. Click **"Create API Key"**
5. Copy the key (starts with `gsk_`)
6. Add to `.env` file:
   ```
   GROQ_API_KEY=gsk_your_key_here
   ```

**OR** paste directly in the Streamlit sidebar when running the app.

### OpenAI API (Optional - Paid)

1. Visit: https://platform.openai.com
2. Create account and add payment method
3. Generate API key
4. Add to `.env`:
   ```
   OPENAI_API_KEY=sk_your_key_here
   ```

---

## 🎥 Demo

### Screenshot
```
┌─────────────────────────────────────────────────────┐
│  📚 Company Policy Chatbot                          │
├─────────────────────────────────────────────────────┤
│  You: What is the leave policy?                     │
│                                                     │
│  Bot: Based on company policies, full-time          │
│       employees get 20 days annual leave...         │
│       📚 Sources: leave_policy.txt                  │
└─────────────────────────────────────────────────────┘
```

### Sample Conversations
```
Q: "What is the company's leave policy?"
A: Provides details about annual, sick, and parental leave with citations

Q: "How many sick days do I get?"
A: Understands context and answers specifically about sick leave

Q: "Can I carry them over to next year?"
A: Remembers "them" refers to sick days, provides accurate answer
```

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    USER QUERY                           │
└────────────────────┬────────────────────────────────────┘
                     ↓
┌────────────────────────────────────────────────────────┐
│  DOCUMENT PROCESSING (document_processor.py)           │
│  • Load PDF/TXT files                                  │
│  • Clean and normalize text                            │
│  • Split into chunks (500 tokens, 50 overlap)          │
└────────────────────┬───────────────────────────────────┘
                     ↓
┌────────────────────────────────────────────────────────┐
│  EMBEDDING GENERATION (rag_engine.py)                  │
│  • SentenceTransformers (all-MiniLM-L6-v2)            │
│  • Convert text to 384-dim vectors                     │
└────────────────────┬───────────────────────────────────┘
                     ↓
┌────────────────────────────────────────────────────────┐
│  VECTOR STORAGE                                        │
│  • FAISS IndexFlatL2                                   │
│  • Fast cosine similarity search                       │
└────────────────────┬───────────────────────────────────┘
                     ↓
┌────────────────────────────────────────────────────────┐
│  RETRIEVAL                                             │
│  • Search top-3 most relevant chunks                   │
│  • Calculate relevance scores                          │
└────────────────────┬───────────────────────────────────┘
                     ↓
┌────────────────────────────────────────────────────────┐
│  GENERATION (LLM)                                      │
│  • Groq (Llama 3.3-70B) or OpenAI GPT                 │
│  • Context-aware response generation                   │
│  • Include conversation history                        │
└────────────────────┬───────────────────────────────────┘
                     ↓
┌────────────────────────────────────────────────────────┐
│  RESPONSE + CITATIONS                                  │
│  • Natural language answer                             │
│  • Source document names                               │
│  • Relevance scores                                    │
└────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Language** | Python 3.8+ | Core programming language |
| **UI Framework** | Streamlit 1.31.0 | Interactive web interface |
| **LLM** | Groq (Llama 3.3-70B) | AI text generation |
| **Embeddings** | SentenceTransformers | Semantic text encoding |
| **Vector DB** | FAISS | Similarity search |
| **PDF Processing** | PyPDF2 | Document parsing |
| **Environment** | python-dotenv | API key management |

---


## 🔍 How It Works

### 1. Document Processing
```python
# document_processor.py
1. Load PDF/TXT files
2. Extract text
3. Clean and normalize
4. Split into 500-token chunks with 50-token overlap
5. Add metadata (source, chunk_id)
```

### 2. Embedding & Storage
```python
# rag_engine.py
1. Convert chunks to 384-dim vectors using SentenceTransformers
2. Store in FAISS index for fast retrieval
3. Maintain document metadata
```

### 3. Query Processing
```python
# When user asks a question:
1. Convert query to embedding vector
2. Search FAISS for top-3 similar chunks (cosine similarity)
3. Retrieve relevant text + source documents
```

### 4. Response Generation
```python
# Generate answer using LLM:
1. Build context from retrieved chunks
2. Add conversation history (last 5 messages)
3. Send to Groq/OpenAI API
4. Return natural language response + citations
```

---

## 🧪 Testing

### Sample Test Questions

**Leave Policy:**
```
✅ "What is the leave policy?"
✅ "How many days of annual leave do I get?"
✅ "Do I need a medical certificate for sick leave?"
✅ "Can I carry over unused leave?"
```

**Remote Work:**
```
✅ "How can I request remote work?"
✅ "Am I eligible for remote work?"
✅ "What equipment is provided?"
✅ "What are the internet requirements?"
```

**IT Security:**
```
✅ "What are the password requirements?"
✅ "How often do I need to change my password?"
✅ "What is the MFA policy?"
```

**Cross-Document:**
```
✅ "Compare leave policy and remote work benefits"
✅ "What are my options if I want flexibility?"
```

**Not in Documents:**
```
✅ "What is the salary structure?" 
   → Should say "not available in policies"
```

### Conversation Memory Test
```
Q1: "What is the leave policy?"
Q2: "How many sick days?"  ← Understands context
Q3: "Can I carry them over?"  ← Remembers "them" = sick days
```

---

## 🐛 Troubleshooting

### Common Issues

**1. Module Not Found Error**
```bash
ModuleNotFoundError: No module named 'streamlit'
```
**Solution:**
```bash
# Ensure venv is activated
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

**2. FAISS Installation Failed**
```bash
ERROR: Could not find a version that satisfies faiss-cpu
```
**Solution:**
```bash
pip install faiss-cpu --no-cache-dir
# OR
pip install faiss-cpu>=1.9.0
```

**3. Model Decommissioned Error**
```
Error: Model llama-3.1-70b-versatile has been decommissioned
```
**Solution:**
Update `rag_engine.py` line ~30:
```python
self.model = "llama-3.3-70b-versatile"  # Use latest model
```

**4. PowerShell Execution Policy**
```
cannot be loaded because running scripts is disabled
```
**Solution:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**5. API Key Not Working**
```bash
# Test if key is loaded
python
>>> import os
>>> from dotenv import load_dotenv
>>> load_dotenv()
>>> print(os.getenv("GROQ_API_KEY"))
```

If returns `None`:
- Check `.env` file exists in project root
- Check no extra spaces in key
- Restart terminal/app

---

## 📊 Performance Metrics

| Operation | Time | Notes |
|-----------|------|-------|
| Document Loading | 0.5-1s | Per document |
| Embedding Generation | 0.3-0.5s | Per query |
| Vector Search | <0.1s | FAISS indexing |
| LLM Response (Groq) | 1-2s | Fast inference |
| LLM Response (OpenAI) | 3-5s | Slower but accurate |
| **Total Response Time** | **2-6s** | End-to-end |

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. **Fork** the repository
2. **Create** a feature branch
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit** your changes
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push** to the branch
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open** a Pull Request

### Areas for Contribution
- [ ] Add DOCX file support
- [ ] Implement multi-language support
- [ ] Add user authentication
- [ ] Create REST API endpoints
- [ ] Add analytics dashboard
- [ ] Support for ChromaDB/Pinecone

---

## 👨‍💻 Author

**Sudeep Mondal**

- 🌐 GitHub: [Sudeep Mondal Deep]([https://github.com/yourusername](https://github.com/sudeepmondal))
- 💼 LinkedIn: [Sudeep Mondal Deep](https://www.linkedin.com/in/smdeep/)
- 📧 Email: smdeep137@gmail.com

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Sudeep Mondal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🙏 Acknowledgments

Special thanks to:
- **Streamlit** - For the amazing UI framework
- **Groq** - For free, fast LLM inference
- **Sentence Transformers** - For state-of-the-art embeddings
- **FAISS** - For efficient vector search
- **OpenAI** - For pioneering LLM technology
- **Meta AI** - For Llama models

---

## 📚 Resources & References

### Documentation
- [RAG Overview](https://aws.amazon.com/what-is/retrieval-augmented-generation/)
- [Groq API Docs](https://console.groq.com/docs)
- [Streamlit Docs](https://docs.streamlit.io/)
- [FAISS Wiki](https://github.com/facebookresearch/faiss/wiki)
- [Sentence Transformers](https://www.sbert.net/)

### Learning Resources
- [Building RAG Systems](https://www.pinecone.io/learn/retrieval-augmented-generation/)
- [Vector Databases Explained](https://www.cloudflare.com/learning/ai/what-is-vector-database/)
- [LLM Best Practices](https://platform.openai.com/docs/guides/prompt-engineering)

---

## 🗺️ Roadmap

### Planned Features
- [ ] DOCX file support
- [ ] Multi-language responses (Bengali, Hindi)
- [ ] User authentication system
- [ ] REST API endpoints
- [ ] Analytics dashboard
- [ ] Conversation export to PDF
- [ ] Voice input/output
- [ ] Mobile-responsive UI
- [ ] Docker containerization
- [ ] Cloud deployment guide

---

## 📞 Support

If you encounter any issues or have questions:

1. **Check** the [Troubleshooting](#-troubleshooting) section
2. **Search** existing [GitHub Issues](https://github.com/yourusername/rag-company-chatbot/issues)
3. **Open** a new issue with:
   - Clear description
   - Steps to reproduce
   - Error messages
   - System info (OS, Python version)

---

## ⭐ Star History

If you find this project helpful, please consider giving it a star!

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/rag-company-chatbot&type=Date)](https://star-history.com/#yourusername/rag-company-chatbot&Date)

---

## 🎓 Educational Purpose

This project was created as part of an **AI Developer assessment** to demonstrate:
- ✅ Understanding of RAG architecture
- ✅ LLM integration skills
- ✅ Vector database implementation
- ✅ Production-ready code quality
- ✅ Clear documentation

Feel free to use this as a learning resource or starting point for your own RAG applications!

---

<div align="center">

**Made with ❤️ by Sudeep Mondal Deep**

*Powered by Python, Streamlit, Groq, and AI*

[⬆ Back to Top](#-rag-based-company-policy-chatbot)

</div>

---

**© 2025 Sudeep Mondal Deep. All rights reserved.**
