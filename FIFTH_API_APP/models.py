from pydantic import BaseModel, Field, field_validator
from typing import Optional
import re

class Task(BaseModel):
    id: int = Field(..., description="Unique identifier for the task")
    title: str = Field(..., description="Title of the task")
    description: Optional[str] = Field(None, description="Detailed description of the task")
    status: str = Field(..., description="Current status of the task")
    assigned_to: Optional[str] = Field(None, description="Person assigned to the task")
    estimated_hours: Optional[float] = Field(None, description="Estimated hours to complete the task")

    @field_validator('status')
    def validate_status(cls, value):
        allowed_statuses = ['To Do', 'In Progress', 'Completed']
        if value not in allowed_statuses:
            raise ValueError(f"Status must be one of {allowed_statuses}")
        return value
    @field_validator('title')
    def validate_title(cls, value):
        if len(value) < 5 or len(value) > 100:
            raise ValueError("Title must be between 5 and 100 characters")
        return value
    @field_validator('description')
    def validate_description(cls, value):
        if value and len(value) > 300:
            raise ValueError("Description must be at most 300 characters")
        return value
    @field_validator('assigned_to')
    def validate_assigned_to(cls, value):
        if not re.match("^[A-Za-z]+$", value):
            raise ValueError("Assigned to must contain only alphabets")
        return value
    @field_validator('estimated_hours')
    def validate_estimated_hours(cls, value):
        if value <= 0 or value > 100:
            raise ValueError("Estimated hours must be greater than 0 and less than or equal to 100")
        return value