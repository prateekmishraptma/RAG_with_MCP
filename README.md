# 🔍 Hybrid RAG System with MCP Integration

A **production-style Retrieval-Augmented Generation (RAG)** system that combines **semantic vector search** with a **Model Context Protocol (MCP)–style external memory service** to deliver accurate, low-hallucination responses.

This project demonstrates how modern LLM applications can integrate **multiple memory sources** (vector + symbolic) using current LangChain Runnable APIs.

---

<img width="985" height="1060" alt="mermaid-diagram" src="https://github.com/user-attachments/assets/a203d11e-5aac-438d-9ebf-2f69df7558d0" />


## 🚀 Key Features

- ✅ **Hybrid RAG Architecture**
  - FAISS-based semantic retrieval
  - MCP-based symbolic / long-term memory
- ✅ **Modern LangChain (Runnable API)**
  - Uses `.invoke()` (no deprecated methods)
- ✅ **FastAPI-based MCP Server**
  - Acts as an external deterministic knowledge store
- ✅ **Hugging Face FLAN-T5 Generator**
  - Instruction-tuned, CPU-friendly model
- ✅ **Clean, modular, interview-ready design**

---

## 🧠 System Architecture

```text
User Query
   |
   ├── MCP Server (symbolic memory, deterministic)
   |
   ├── Vector Retriever (FAISS + embeddings)
   |
   └── Context Merger
           |
           v
     FLAN-T5 Generator

This hybrid approach reduces hallucinations and improves factual grounding.

📂 Project Structure
.
├── RAG_MCP.ipynb        # Complete RAG pipeline (vector + MCP + LLM)
├── mcp_server.py       # FastAPI MCP memory server
├── README.md           # Project documentation
⚙️ Tech Stack

Python 3.10+

LangChain (Runnable API)

FAISS

HuggingFace Transformers

FLAN-T5 (google/flan-t5-base)

FastAPI

Pydantic

🏃‍♂️ How to Run the Project
1️⃣ Install Dependencies
pip install langchain langchain-community transformers faiss-cpu fastapi uvicorn pydantic
2️⃣ Start the MCP Server
python mcp_server.py

Server runs at:

http://127.0.0.1:8000

Swagger UI:

http://127.0.0.1:8000/docs
3️⃣ Run the RAG Pipeline

Open and execute:

RAG_MCP.ipynb

The notebook:

Loads documents

Builds FAISS index

Queries MCP memory

Merges contexts

Generates final answer using FLAN-T5

🔌 MCP Server API
Endpoint
POST /mcp/query
Request
{
  "query": "What is ProjectPro?"
}
Response
{
  "response": "ProjectPro is a platform offering solved end-to-end data science and AI projects."
}
🎯 Why MCP + RAG?
Component	Purpose
Vector Store	Semantic similarity search
MCP Server	Deterministic, long-term knowledge
LLM	Natural language generation

This mirrors real-world LLM systems used in production.

📌 Highlights for Interviews

Built hybrid memory RAG

Used FastAPI as external tool / memory

Avoided deprecated LangChain APIs

Reduced hallucinations via symbolic memory

Designed for extensibility (tools, agents, multi-memory)

🔮 Future Enhancements

Tool-calling based MCP routing

Agentic RAG (planner + executor)

Caching & retry logic

Multi-source MCP memory

Streaming responses

📜 License

This project is for educational and portfolio purposes.

🙌 Acknowledgements

Inspired by modern RAG, MCP concepts, and LangChain’s Runnable architecture.
