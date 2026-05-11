from sqlachemy import Column, Integer, String
from database import Base

class Patient(Base):
    __tablename__ = "patients"

    patient_id = Column(Integer, primary_key=True, index=True)

    patient_name = Column(String(100), nullable=False)

    age = Column(Integer)

    mobile = Column(String(20))
    
    
class Doctor(Base):
    __tablename__ = "doctors"

    doctor_id = Column(Integer, primary_key=True, index=True)

    doctor_name = Column(String(100), nullable=False)

    specialization = Column(String(50))
    
class Appointment(Base):
    __tablename__ = "appointments"

    appointment_id = Column(Integer, primary_key=True, index=True)

    patient_id = Column(Integer)

    doctor_id = Column(Integer)

    appointment_date = Column(String(20))