from pydantic import BaseModel

class Patients(BaseModel):
    patient_id: int
    patient_name: str
    age: int
    mobile: str

    class Config:
        from_attributes = True
        
class Doctors(BaseModel):
    doctor_id: int
    doctor_name: str
    specialization: str

    class Config:
        from_attributes = True
        
class Appointments(BaseModel):
    appointment_id: int
    patient_id: int
    doctor_id: int
    appointment_date: str

    class Config:
        from_attributes = True