from fastapi import HTTPException

def validate_operation(operation: str):
    valid_operations = ["add", "sub", "mul", "div"]
    if operation not in valid_operations:
        raise HTTPException(
            status_code=400,
            detail="Invalid Operation"
        )