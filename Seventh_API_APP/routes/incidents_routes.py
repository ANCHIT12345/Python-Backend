from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from fastapi.security import HTTPBearer
import models, schemas, auth
from database import get_db

router = APIRouter(
    prefix="/soc", tags=["Incident Reports"])
security = HTTPBearer()

@router.post("/login", response_model=schemas.TokenResponse)
def login(request: schemas.LoginRequest, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == request.username).first()
    if not user or not auth.verify_password(request.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = auth.create_access_token(
        data={"sub": user.username, "role": user.role, "team": user.team}, expires_delta=timedelta(hours=2)
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/logout")
def logout(credentials=Depends(security)):
    auth.BLACKLIST.add(credentials.credentials)
    return {"message": "Successfully logged out. Token revoked."}

@router.get("/incidents")
def get_incidents(token_data=Depends(auth.RequireRole(["Analyst", "Manager", "Admin"])), db: Session = Depends(get_db)):
    return {"incidents": db.query(models.Incident).all()}

@router.put("/incidents/assign/{incident_id}")
def assign_incident(incident_id: int, token_data=Depends(auth.RequireRole(["Manager", "Admin"])), db: Session = Depends(get_db)):
    incident = db.query(models.Incident).filter(models.Incident.id == incident_id).first()
    if not incident: raise HTTPException(status_code=404, detail="Incident not found")
    
    user = db.query(models.User).filter(models.User.username == token_data.sub).first()
    incident.assigned_to_id = user.id
    db.commit()
    return {"message": f"Incident {incident_id} assigned to {token_data.sub}."}

@router.post("/incidents/close/{incident_id}")
def close_incident(incident_id: int, token_data=Depends(auth.RequireRole(["Admin"])), db: Session = Depends(get_db)):
    incident = db.query(models.Incident).filter(models.Incident.id == incident_id).first()
    if not incident: raise HTTPException(status_code=404, detail="Incident not found")
    
    incident.status = "Closed"
    log = models.AuditLog(action=f"Closed Incident {incident_id}", username=token_data.sub)
    db.add(log)
    db.commit()
    return {"message": f"Incident {incident_id} permanently closed."}

@router.get("/security/audit-logs")
def get_audit_logs(token_data=Depends(auth.RequireRole(["Admin"])), db: Session = Depends(get_db)):
    return {"logs": db.query(models.AuditLog).all()}
