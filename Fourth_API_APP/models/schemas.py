from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum

class Priority(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    
class Status(str, Enum):
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"
    
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=5)
    description: Optional[str] = None
    priority: Priority
    assigned_to: str
    
class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=5)
    priority: Optional[Priority]
    status: Optional[Status]
    
class TaskInternal(BaseModel):
    task_id: int
    title: str
    description: Optional[str]
    priority: Priority
    status: Status
    assigned_to: str
    created_at: datetime
    internal_notes: str = ""
    
class TaskResponse(BaseModel):
    task_id: int
    title: str
    priority: Priority
    status: Status
    
class TaskListV2(BaseModel):
    count: int
    tasks: List[TaskResponse]
