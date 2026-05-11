from pydantic import BaseModel
from datetime import datetime

class PatientBase(BaseModel):
    name: str
    age: int
    mobile: str
    
class PatientCreate(PatientBase):
    pass

class PatientResponse(PatientBase):
    id: int
    
    class Config:
        from_attribute = True

class DoctorBase(BaseModel):
    name: str
    specialization: str
    
class DoctorCreate(DoctorBase):
    pass


class DoctorResponse(DoctorBase):
    id: int
    
    class Config:
        from_attribute = True


class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_date: datetime
    
    
class AppointmentCreate(AppointmentBase):
    pass

class AppointmentResponse(AppointmentBase):
    id: int
    
    class Config:
        from_attribute = True
        
        
