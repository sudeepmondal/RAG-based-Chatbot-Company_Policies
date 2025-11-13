import streamlit as st
import os
from pathlib import Path
from dotenv import load_dotenv
from document_processor import DocumentProcessor
from rag_engine import RAGEngine

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(
    page_title="Company Policy Chatbot",
    page_icon="📚",
    layout="wide"
)

# Initialize session state
if 'rag_engine' not in st.session_state:
    st.session_state.rag_engine = None
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'documents_loaded' not in st.session_state:
    st.session_state.documents_loaded = False

# Title
st.title("📚 Company Policy Chatbot")
st.markdown("*Powered by RAG (Retrieval-Augmented Generation)*")

# Sidebar
with st.sidebar:
    st.header("🔧 Configuration")
    
    # API Key selection
    api_provider = st.radio(
        "Select API Provider",
        ["Free Mode (No API)", "Groq (FREE!)", "OpenAI"],
        help="Groq is completely free and fast!",
        key="api_provider_radio"
    )
    
    api_key = None
    groq_key = None
    
    if api_provider == "Groq (FREE!)":
        groq_key = st.text_input(
            "Groq API Key",
            type="password",
            help="Get free key from https://console.groq.com",
            key="groq_key_input"
        )
        if not groq_key:
            groq_key = os.getenv("GROQ_API_KEY")
        
        if groq_key:
            st.success(f"✅ Groq key loaded: {groq_key[:15]}...{groq_key[-5:]}")
            
    elif api_provider == "OpenAI":
        api_key = st.text_input(
            "OpenAI API Key",
            type="password",
            help="Your OpenAI API key",
            key="openai_key_input"
        )
        if not api_key:
            api_key = os.getenv("OPENAI_API_KEY")
        
        if api_key:
            st.success(f"✅ OpenAI key loaded: {api_key[:15]}...{api_key[-5:]}")
    else:
        st.info("ℹ️ Running in Free Mode - No API calls")
    
    st.divider()
    
    # Document upload
    st.header("📄 Upload Documents")
    uploaded_files = st.file_uploader(
        "Upload company policy documents",
        type=['pdf', 'txt'],
        accept_multiple_files=True
    )
    
    # Debug info
    if groq_key:
        st.success(f"✅ Groq key detected: {groq_key[:20]}...")
    elif api_key:
        st.info(f"ℹ️ OpenAI key detected: {api_key[:20]}...")
    else:
        st.warning("⚠️ No API key - using free mode")
    
    # Initialize RAG button
    if st.button("🚀 Initialize RAG System", type="primary"):
        if uploaded_files:
            with st.spinner("Processing documents..."):
                # Save uploaded files temporarily
                temp_dir = Path("temp_docs")
                temp_dir.mkdir(exist_ok=True)
                
                file_paths = []
                for uploaded_file in uploaded_files:
                    file_path = temp_dir / uploaded_file.name
                    with open(file_path, "wb") as f:
                        f.write(uploaded_file.getvalue())
                    file_paths.append(str(file_path))
                
                # Process documents
                processor = DocumentProcessor()
                chunks = processor.process_documents(file_paths)
                
                # Initialize RAG engine
                st.session_state.rag_engine = RAGEngine(
                    openai_api_key=api_key if api_key else None,
                    groq_api_key=groq_key if groq_key else None
                )
                st.session_state.rag_engine.add_documents(chunks)
                st.session_state.documents_loaded = True
                
                st.success(f"✅ Processed {len(chunks)} chunks from {len(uploaded_files)} documents!")
        else:
            st.warning("⚠️ Please upload documents first!")
    
    st.divider()
    
    # System info
    st.header("ℹ️ System Info")
    if st.session_state.documents_loaded:
        st.success("✅ RAG System Ready")
        st.metric("Documents in Vector Store", 
                 len(st.session_state.rag_engine.documents))
    else:
        st.info("📤 Upload documents to get started")
    
    # Conversation Stats
    if st.session_state.messages:
        st.divider()
        st.header("💬 Conversation Stats")
        
        user_msgs = len([m for m in st.session_state.messages if m["role"] == "user"])
        bot_msgs = len([m for m in st.session_state.messages if m["role"] == "assistant"])
        
        col1, col2 = st.columns(2)
        col1.metric("👤 Your Questions", user_msgs)
        col2.metric("🤖 Bot Replies", bot_msgs)
        
        # Show recent topics
        if user_msgs > 0:
            st.caption("📝 Recent Questions:")
            recent_questions = [
                m["content"][:40] + "..." 
                for m in st.session_state.messages[-6:] 
                if m["role"] == "user"
            ]
            for q in recent_questions[-3:]:
                st.caption(f"• {q}")
    
    # Clear chat button
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()
    
    # Export chat button
    if st.session_state.messages and st.button("💾 Export Chat"):
        # Create formatted text
        chat_export = "=" * 50 + "\n"
        chat_export += "Company Policy Chatbot - Chat History\n"
        chat_export += "=" * 50 + "\n\n"
        
        for i, msg in enumerate(st.session_state.messages, 1):
            role = "YOU" if msg["role"] == "user" else "BOT"
            chat_export += f"[{i}] {role}:\n{msg['content']}\n"
            
            if msg["role"] == "assistant" and "sources" in msg:
                sources = ", ".join(set([s["source"] for s in msg["sources"]]))
                chat_export += f"   📚 Sources: {sources}\n"
            
            chat_export += "\n" + "-" * 50 + "\n\n"
        
        # Download button
        st.download_button(
            label="⬇️ Download Chat History",
            data=chat_export,
            file_name=f"chat_history.txt",
            mime="text/plain",
            key="download_chat"
        )

# Main chat interface
st.header("💬 Chat with Your Policies")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
        # Show sources if available
        if message["role"] == "assistant" and "sources" in message:
            with st.expander("📚 View Sources"):
                for i, source in enumerate(message["sources"], 1):
                    st.markdown(f"**Source {i}: {source['source']}**")
                    st.text(source['text'][:200] + "...")
                    st.caption(f"Relevance Score: {source['score']:.4f}")

# Chat input
if prompt := st.chat_input("Ask about company policies..."):
    if not st.session_state.documents_loaded:
        st.error("⚠️ Please upload and initialize documents first!")
    else:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                # Get conversation history (last 5 messages)
                history = [
                    {"role": msg["role"], "content": msg["content"]}
                    for msg in st.session_state.messages[-5:]
                ]
                
                # Query RAG system
                result = st.session_state.rag_engine.query(
                    prompt,
                    top_k=3,
                    conversation_history=history
                )
                
                # Display answer
                st.markdown(result['answer'])
                
                # Show sources
                with st.expander("📚 View Sources"):
                    for i, source in enumerate(result['sources'], 1):
                        st.markdown(f"**Source {i}: {source['source']}**")
                        st.text(source['text'][:200] + "...")
                        st.caption(f"Relevance Score: {source['score']:.4f}")
                
                # Add to messages
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": result['answer'],
                    "sources": result['sources']
                })

# Sample questions
with st.expander("💡 Sample Questions"):
    st.markdown("""
    - What is the company's leave policy?
    - How can employees request remote work?
    - What are the password requirements?
    - Tell me about parental leave
    - What equipment is provided for remote work?
    """)

# Footer
st.divider()
st.caption("Built with using Streamlit, FAISS, Sentence Transformers and Groq")