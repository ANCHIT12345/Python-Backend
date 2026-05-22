from fastapi import Depends, HTTPException
from models.schemas import Priority, Status

def log_request():
    print("Request received")

def validate_priority(priority: Priority):
    if priority not in Priority:
        raise HTTPException(status_code=400, detail="Invalid priority value")
    return priority

def default_status():
    return Status.OPEN