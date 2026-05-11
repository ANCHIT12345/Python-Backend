from sqlalchemy import Session
from models import Doctor, Patient, Appointment

def create_doctor(db: Session, doctor: Doctor):
    db.add(doctor)
    db.commit()
    db.refresh(doctor)
    return doctor

def create_patient(db: Session, patient: Patient):
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient

def create_appointment(db: Session, appointment: Appointment):
    db.add(appointment)
    db.commit()
    db.refresh(appointment)
    return appointment

def get_doctor(db: Session, doctor_id: int):
    return db.query(Doctor).filter(Doctor.id == doctor_id).first()

def get_patient(db: Session, patient_id: int):
    return db.query(Patient).filter(Patient.id == patient_id).first()

def get_appointment(db: Session, appointment_id: int):
    return db.query(Appointment).filter(Appointment.id == appointment_id).first()

def update_doctor(db: Session, doctor_id: int, updated_doctor: Doctor):
    doctor = get_doctor(db, doctor_id)
    if doctor:
        doctor.name = updated_doctor.name
        doctor.specialization = updated_doctor.specialization
        db.commit()
        db.refresh(doctor)
    return doctor

def update_patient(db: Session, patient_id: int, updated_patient: Patient):
    patient = get_patient(db, patient_id)
    if patient:
        patient.name = updated_patient.name
        patient.age = updated_patient.age
        db.commit()
        db.refresh(patient)
    return patient

def update_appointment(db: Session, appointment_id: int, updated_appointment: Appointment):
    appointment = get_appointment(db, appointment_id)
    if appointment:
        appointment.doctor_id = updated_appointment.doctor_id
        appointment.patient_id = updated_appointment.patient_id
        appointment.date = updated_appointment.date
        db.commit()
        db.refresh(appointment)
    return appointment

def delete_doctor(db: Session, doctor_id: int):
    doctor = get_doctor(db, doctor_id)
    if doctor:
        db.delete(doctor)
        db.commit()
    return doctor

def delete_patient(db: Session, patient_id: int):
    patient = get_patient(db, patient_id)
    if patient:
        db.delete(patient)
        db.commit()
    return patient

def delete_appointment(db: Session, appointment_id: int):
    appointment = get_appointment(db, appointment_id)
    if appointment:
        db.delete(appointment)
        db.commit()
    return appointment


