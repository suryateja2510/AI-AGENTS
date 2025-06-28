from typing import Optional

from fastapi import APIRouter, Query
from app.services.agents.data_analyzer_agent.agent import run_data_analyzer_agent
from app.services.agents.demo_agent.agent import run_demo_agent

router = APIRouter()


@router.post("/demo-agent")
def demo_agent(
    user_query: str = Query(..., description="Your question for the AI agent"),
    thread_id: Optional[str] = Query(
        None, description="Thread ID to maintain conversation"
    ),
):
    return run_demo_agent(user_query, thread_id)


@router.post("/data-analyzer-agent")
def data_analyzer_agent(
    user_query: str = Query(
        ..., description="Your question for the data analyzer agent"
    ),
    thread_id: str = Query(None, description="Thread ID to maintain conversation"),
):
    return run_data_analyzer_agent(user_query, thread_id)
