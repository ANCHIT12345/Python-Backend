from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import timedelta
import models, schemas, auth
from database import get_db

router = APIRouter(prefix="/hr", tags=["Assignment 2: HR Management"])

@router.post("/login", response_model=schemas.TokenResponse)
def login(request: schemas.LoginRequest, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == request.username).first()
    if not user or not auth.verify_password(request.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = auth.create_access_token(
        data={"sub": user.username, "role": user.role}, expires_delta=timedelta(hours=1)
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/employee/dashboard")
def dashboard(token_data: schemas.TokenPayLoad = Depends(auth.RequireRole(["Employee", "HR", "Admin"]))):
    return {"message": f"Welcome, {token_data.sub}!"}

@router.get("/employees")
def list_employees(token_data: schemas.TokenPayLoad = Depends(auth.RequireRole(["HR", "Admin"])), db: Session = Depends(get_db)):
    employees = db.query(models.EmployeeData).all()
    return {"employees": employees}

@router.delete("/admin/remove-employee/{emp_id}")
def remove_employee(emp_id: int, token_data: schemas.TokenPayLoad = Depends(auth.RequireRole(["Admin"])), db: Session = Depends(get_db)):
    emp = db.query(models.EmployeeData).filter(models.EmployeeData.id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(emp)
    db.commit()
    return {"message": f"Employee {emp_id} removed by {token_data.sub}"}