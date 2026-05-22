from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, validator
from typing import Optional, List
from models import Task
from exception import taskAlreadyExistsException, taskNotFoundException
import logging
from logger import logger
app = FastAPI()

tasks_db = {}

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    if task.id in tasks_db:
        logger.error(f"Task with id {task.id} already exists")
        raise taskAlreadyExistsException()
    tasks_db[task.id] = task
    return task

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return list(tasks_db.values())

@app.get("/tasks/{id}", response_model=Task)
def get_task(id: int):
    if id not in tasks_db:
        logger.error(f"Task with id {id} not found")
        raise taskNotFoundException()
    return tasks_db[id]

@app.put("/tasks/{id}", response_model=Task)
def update_task(id: int, task: Task):
    if id not in tasks_db:
        logger.error(f"Task with id {id} not found for update")
        raise taskNotFoundException()
    if tasks_db[id].status == "Completed" and task.status == "In Progress":
        logger.error(f"Invalid status transition for task id {id}")
        raise HTTPException(status_code=400, detail="Invalid status transition")
    tasks_db[id] = task
    return task

@app.delete("/tasks/{id}")
def delete_task(id: int):
    if id not in tasks_db:
        logger.error(f"Task with id {id} not found for deletion")
        raise taskNotFoundException()
    del tasks_db[id]
    return {"message": "Task deleted successfully"}

@app.exception_handler(taskAlreadyExistsException)
def handle_task_already_exists_exception(request: Request, exc: taskAlreadyExistsException):
    logger.error(f"Task already exists: {exc}")
    return JSONResponse(
        status_code=400,
        content={"error": str(exc), "status_code": 400}
    )

@app.exception_handler(taskNotFoundException)
def handle_task_not_found_exception(request: Request, exc: taskNotFoundException):
    logger.error(f"Task not found: {exc}")
    return JSONResponse(
        status_code=404,
        content={"error": str(exc), "status_code": 404}
    )
    
@app.exception_handler(Exception)
def handle_generic_exception(request: Request, exc: Exception):
    logger.error(f"Internal Server Error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error"}
    )
    
    
# Assignment: Build a Task Management API

# Business Context

# You are building a backend service for a Task Management System (like Jira/Trello).

# Employees can:

#     Create tasks
#     Assign tasks
#     Track status
#     Update progress

# The system must be:

#     Strictly validated
#     Secure in error handling
#     Traceable via logs

# Objective

# Using FastAPI and Pydantic, implement:

#     Request validation (Pydantic v2)
#     Custom exception handling
#     Global exception handling
#     File-based logging

# Functional Requirements

# 1.Create Task API

# Endpoint:

# POST /tasks

# Sample Input:

# {
#   "id": 1,
#   "title": "Fix login bug",
#   "description": "User unable to login with valid credentials",
#   "priority": "High",
#   "status": "Pending",
#   "assigned_to": "Vinod",
#   "estimated_hours": 5
# }

# 2.Validation Rules (Pydantic)

#     id → required, positive integer
#     title → min 5 chars, max 100
#     description → optional, max 300 chars
#     priority → must be one of: Low, Medium, High
#     status → must be one of: Pending, In Progress, Completed
#     assigned_to → only alphabets allowed (no numbers)
#     estimated_hours → must be > 0 and ≤ 100

# Must use:

#     Field(...)
#     pattern=
#     @field_validator

# 3. Custom Exceptions (Business Rules)

# Create custom exceptions:

# a) TaskAlreadyExistsException

#  Trigger:

#     If task with same id already exists

# b) InvalidTaskStateException

#  Trigger:

#     If someone tries:
#         Moving task from Completed → In Progress
#         Or invalid status transitions

# 4.⃣ Global Exception Handling

# Handle all unexpected errors:

# Response:

# {
#   "message": "Internal Server Error"
# }

# Do NOT expose internal details

# 5.Custom Exception Handlers

# Example Response:

# {
#   "error": "Task already exists",
#   "status_code": 400
# }

# 6. Logging (File-Based)

# Log all errors into:

# logs/app.log

# Log Format:

#     Timestamp
#     API name
#     Error message

# Use Python logging

# 7. Additional APIs

# GET /tasks

# → Return all tasks

# GET /tasks/{id}

# → Return task by ID

# PUT /tasks/{id}

# → Update task

# DELETE /tasks/{id}

# → Delete task

# Expected Project Structure

# task-management/
# │── main.py
# │── models.py
# │── exceptions.py
# │── logger.py
# │── logs/
# │    └── app.log