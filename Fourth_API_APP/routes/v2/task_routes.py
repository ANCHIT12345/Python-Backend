from fastapi import APIRouter, Depends, Query
from models.schemas import TaskResponse, TaskListV2
from services.task_service import get_tasks_filtered
from dependencies.common import log_request

router = APIRouter(prefix="/api/v2/tasks", tags=["V2 Tasks"])

@router.get("", response_model=TaskListV2)
def list_tasks_v2(
    priority: str = Query(None),
    _: None = Depends(log_request)
):
    tasks = get_tasks_filtered(priority)
    return {
        "count": len(tasks),
        "tasks": tasks
    }