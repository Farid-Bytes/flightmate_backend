from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.agents.main_agent import process_user_request

app = FastAPI()

class UserRequest(BaseModel):
    message: str

@app.post("/query-agent")
async def query_agent(req: UserRequest):
    response = process_user_request(req.message)
    return {"response": response}
