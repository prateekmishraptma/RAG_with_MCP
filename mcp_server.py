from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn
import nest_asyncio

nest_asyncio.apply()
app=FastAPI()
#Simulated long-term memory or external SystemError

agent_memory={
    "projectpro": "ProjectPro is a platform offering solved end-to-end data science and AI projects.",
    "langchain": "Langchain helps build LLM-powered applications by chaining components like prompts, retrievers, tools."
    }

class QueryRequest(BaseModel):
    query: str

@app.post("/mcp/query")
async def handle_query(req: QueryRequest):
    q = req.query.lower()
    for key in agent_memory:
        if key in q:
            return {"response": agent_memory[key]}
    return {"response": "No memory found for the query."}
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)