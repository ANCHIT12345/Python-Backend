from pydantic import BaseModel # pyright: ignore[reportMissingImports]
from datetime import datetime


#test
class PatientBase(BaseModel):

    patient_name: str
    age: int
    mobile: str


class PatientCreate(PatientBase):
    pass


class PatientResponse(PatientBase):

    patient_id: int

    class Config:
        from_attributes = True




class DoctorBase(BaseModel):

    doctor_name: str
    specialization: str


class DoctorCreate(DoctorBase):
    pass


class DoctorResponse(DoctorBase):

    doctor_id: int

    class Config:
        from_attributes = True




class AppointmentBase(BaseModel):

    patient_id: int
    doctor_id: int
    appointment_date: datetime


class AppointmentCreate(AppointmentBase):
    pass


class AppointmentResponse(AppointmentBase):

    appointment_id: int

    class Config:
        from_attributes = True