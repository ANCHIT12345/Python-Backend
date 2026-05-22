from sqlalchemy.orm import Session# pyright: ignore[reportMissingImports]

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

    return (
        db.query(Doctor)
        .filter(Doctor.doctor_id == doctor_id)
        .first()
    )


def get_patient(db: Session, patient_id: int):

    return (
        db.query(Patient)
        .filter(Patient.patient_id == patient_id)
        .first()
    )


def get_appointment(db: Session, appointment_id: int):

    return (
        db.query(Appointment)
        .filter(Appointment.appointment_id == appointment_id)
        .first()
    )



def update_doctor(
    db: Session,
    doctor_id: int,
    updated_doctor: Doctor
):

    doctor = get_doctor(db, doctor_id)

    if doctor:

        doctor.doctor_name = updated_doctor.doctor_name

        doctor.specialization = updated_doctor.specialization

        db.commit()

        db.refresh(doctor)

    return doctor


def update_patient(
    db: Session,
    patient_id: int,
    updated_patient: Patient
):

    patient = get_patient(db, patient_id)

    if patient:

        patient.patient_name = updated_patient.patient_name

        patient.age = updated_patient.age

        patient.mobile = updated_patient.mobile

        db.commit()

        db.refresh(patient)

    return patient


def update_appointment(
    db: Session,
    appointment_id: int,
    updated_appointment: Appointment
):

    appointment = get_appointment(
        db,
        appointment_id
    )

    if appointment:

        appointment.doctor_id = updated_appointment.doctor_id

        appointment.patient_id = updated_appointment.patient_id

        appointment.appointment_date = (
            updated_appointment.appointment_date
        )

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


def delete_appointment(
    db: Session,
    appointment_id: int
):

    appointment = get_appointment(
        db,
        appointment_id
    )

    if appointment:

        db.delete(appointment)

        db.commit()

    return appointment


def search_patient_by_mobile(
    db: Session,
    mobile: str
):

    return (
        db.query(Patient)
        .filter(Patient.mobile == mobile)
        .first()
    )