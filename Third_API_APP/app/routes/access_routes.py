from fastapi import APIRouter, HTTPException, Query
from app.models.schemas import EmployeeCreate, LoginAttempt
from app.services.access_service import (
    register_employee,
    get_employee,
    list_employees,
    process_login_attempt,
    calculate_risk
)

router = APIRouter()

@router.post("/employees")
def create_employee(data: EmployeeCreate):
    register_employee(data)
    return {"message": "Employee registered"}

@router.get("/employees/{employee_id}")
def employee_details(employee_id: int):

    emp = get_employee(employee_id)

    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    return emp

@router.get("/employees")
def employees_list(department: str = Query(None)):
    return list_employees(department)

@router.post("/login-attempt")
def login_attempt(data: LoginAttempt):

    emp, status = process_login_attempt(data)

    if status == "not_found":
        raise HTTPException(status_code=404, detail="Employee not found")

    if status == "locked":
        raise HTTPException(status_code=403, detail="Account locked")

    return {"message": "Login attempt recorded"}

@router.get("/risk/{employee_id}")
def risk_score(employee_id: int):

    result = calculate_risk(employee_id)

    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")

    return result