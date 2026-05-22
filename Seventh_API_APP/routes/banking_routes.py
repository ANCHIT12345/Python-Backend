from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import timedelta
import models, schemas, auth
from database import get_db

router = APIRouter(prefix="/banking", tags=["Assignment 1: Banking API"])

@router.post("/login", response_model=schemas.TokenResponse)
def login(request: schemas.LoginRequest, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == request.username).first()
    if not user or not auth.verify_password(request.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = auth.create_access_token(
        data={"sub": user.username, "role": user.role},
        expires_delta=timedelta(minutes=15) 
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/account/profile")
def get_profile(token_data: schemas.TokenPayLoad = Depends(auth.verify_token), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == token_data.sub).first()
    profile = db.query(models.BankingProfile).filter(models.BankingProfile.user_id == user.id).first()
    return {"user": user.username, "account_number": profile.account_number, "balance": profile.balance}

@router.get("/transactions")
def get_transactions(token_data: schemas.TokenPayLoad = Depends(auth.verify_token), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == token_data.sub).first()
    transactions = db.query(models.Transaction).filter(models.Transaction.user_id == user.id).all()
    return {"transactions": transactions}