from pydantic import BaseModel, Field

class EmployeeCreate(BaseModel):
    employee_id: int
    name: str = Field(..., min_length=3)
    department: str 
    age: int = Field(..., gt=18)
    
class LoginAttempt(BaseModel):
    employee_id: int
    success: bool