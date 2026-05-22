from fastapi import APIRouter, Depends, HTTPException
from models.schemas import TaskCreate, TaskUpdate, TaskResponse
from services.task_service import create_task, update_task, get_tasks
from dependencies.common import log_request, default_status

router = APIRouter(prefix="/api/v1/tasks", tags=["V1 tasks"])

@router.post(
    "",
    response_model=TaskResponse,
    summary="Create task",
    description="Create a new task"
)
def create(
    data: TaskCreate,
    status=Depends(default_status),
    _:None=Depends(log_request)
):
    try: 
        task = create_task(data, status)
        return task
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.put("/{task_id}", response_model=TaskResponse)
def update(task_id: int, data: TaskUpdate, _: None = Depends(log_request)):
    try:
        task = update_task(task_id, data)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return task
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("", response_model=list[TaskResponse])
def list_tasks(_: None = Depends(log_request)):
    return get_tasks()
    