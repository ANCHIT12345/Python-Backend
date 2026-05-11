from fastapi import FastAPI, Depends, HTTPException  # pyright: ignore[reportMissingImports]
from sqlalchemy.orm import Session # pyright: ignore[reportMissingImports]

import models
import schemas
import crud

from database import engine, get_db

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Hospital Management API",
    version="1.0"
)



@app.post(
    "/patients",
    response_model=schemas.PatientResponse
)
def create_patient(
    patient: schemas.PatientCreate,
    db: Session = Depends(get_db)
):

    new_patient = models.Patient(
        patient_name=patient.patient_name,
        age=patient.age,
        mobile=patient.mobile
    )

    return crud.create_patient(
        db,
        new_patient
    )



@app.post(
    "/doctors",
    response_model=schemas.DoctorResponse
)
def create_doctor(
    doctor: schemas.DoctorCreate,
    db: Session = Depends(get_db)
):

    new_doctor = models.Doctor(
        doctor_name=doctor.doctor_name,
        specialization=doctor.specialization
    )

    return crud.create_doctor(
        db,
        new_doctor
    )



@app.post(
    "/appointments",
    response_model=schemas.AppointmentResponse
)
def create_appointment(
    appointment: schemas.AppointmentCreate,
    db: Session = Depends(get_db)
):

    new_appointment = models.Appointment(
        patient_id=appointment.patient_id,
        doctor_id=appointment.doctor_id,
        appointment_date=appointment.appointment_date
    )

    return crud.create_appointment(
        db,
        new_appointment
    )



@app.get(
    "/patients/{patient_id}",
    response_model=schemas.PatientResponse
)
def get_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):

    patient = crud.get_patient(
        db,
        patient_id
    )

    if not patient:

        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return patient


@app.get("/appointments/{appointment_id}")
def get_appointment(
    appointment_id: int,
    db: Session = Depends(get_db)
):

    appointment = crud.get_appointment(
        db,
        appointment_id
    )

    if not appointment:

        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )

    return {
        "appointment_id": appointment.appointment_id,

        "appointment_date": appointment.appointment_date,

        "patient": {
            "patient_id": appointment.patient.patient_id,
            "patient_name": appointment.patient.patient_name
        },

        "doctor": {
            "doctor_id": appointment.doctor.doctor_id,
            "doctor_name": appointment.doctor.doctor_name,
            "specialization": appointment.doctor.specialization
        }
    }



@app.delete("/appointments/{appointment_id}")
def delete_appointment(
    appointment_id: int,
    db: Session = Depends(get_db)
):

    appointment = crud.delete_appointment(
        db,
        appointment_id
    )

    if not appointment:

        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )

    return {
        "message": "Appointment deleted successfully"
    }



@app.get("/patients/search/{mobile}")
def search_patient(
    mobile: str,
    db: Session = Depends(get_db)
):

    patient = crud.search_patient_by_mobile(
        db,
        mobile
    )

    if not patient:

        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return patient

# Problem Statement

# A hospital wants to build a secure backend API for managing:

#     patients
#     doctors
#     appointments

# The system must:

#     store records in SQL Server
#     maintain relationships between tables
#     expose secure CRUD APIs
#     prevent SQL injection attacks

# Database Requirements

# Create database tables:

# 1.Patients Table

# Column
	

# Type

# patient_id
	

# INT (PK)

# patient_name
	

# VARCHAR

# age
	

# INT

# mobile
	

# VARCHAR

# 2.Doctors Table

# Column
	

# Type

# doctor_id
	

# INT (PK)

# doctor_name
	

# VARCHAR

# specialization
	

# VARCHAR

# 3.Appointments Table

# Column
	

# Type

# appointment_id
	

# INT (PK)

# patient_id
	

# FK

# doctor_id
	

# FK

# appointment_date
	

# DATETIME

# Assignment Tasks

# Part A – SQL Server & Relationships

# Task 1

# Create all tables with:

#     primary keys
#     foreign keys
#     NOT NULL constraints

# Task 2

# Insert sample records using SQL queries.

# Part B – SQLAlchemy ORM

# Task 3

# Create SQLAlchemy ORM models for:

#     Patient
#     Doctor
#     Appointment

# Task 4

# Establish relationships using ORM mapping.

# Part C – Secure CRUD APIs

# Task 5

# Create API:

# POST /patients

# Store patient in SQL Server.

# Task 6

# Create API:

# GET /appointments/{patient_id}

# Return:

#     patient details
#     doctor details
#     appointment date

# Task 7

# Create API:

# DELETE /appointments/{appointment_id}

# Security Tasks

# Task 8

# Prevent SQL injection while searching patient by mobile number.

# Vulnerable example:

# SELECT * FROM patients WHERE mobile='{mobile}'

# Students must implement safe parameterized query.

# Task 9

# Use least-privilege DB access:

#     API should NOT use sysadmin account
#     create restricted DB user

# Assignment 2 – Online Banking Transaction API

# Domain: Banking System

# Problem Statement

# A bank needs secure APIs to:

#     manage customer accounts
#     transfer money
#     view transaction history

# Security is critical because financial data is sensitive.

# Database Requirements

# 1.Customers Table

# Column
	

# Type

# customer_id
	

# INT

# customer_name
	

# VARCHAR

# email
	

# VARCHAR

# 2.Accounts Table

# Column
	

# Type

# account_id
	

# INT

# customer_id
	

# FK

# balance
	

# DECIMAL

# 3.Transactions Table

# Column
	

# Type

# transaction_id
	

# INT

# account_id
	

# FK

# amount
	

# DECIMAL

# transaction_type
	

# VARCHAR

# Assignment Tasks

# Part A – SQL Design

# Task 1

# Create tables with:

#     relationships
#     balance constraints
#     unique email constraint

# Task 2

# Insert test banking data.

# Part B – FastAPI + SQLAlchemy

# Task 3

# Create API:

# POST /accounts

# Create new bank account.

# Task 4

# Create API:

# POST /transfer

# Transfer money between accounts.

# Rules:

#     insufficient balance → reject
#     invalid account → reject

# Task 5

# Create API:

# GET /transactions/{account_id}

# Return account transaction history.

#  Security Tasks

# Task 6 – SQL Injection Attack Simulation

# Students must:

#     first create vulnerable login query
#     then fix it using parameterized query

# Attack example:

# ' OR 1=1 --

# Task 7 – Transaction Safety

# Use:

# commit()
# rollback()

# Ensure failed transfer does not partially update balances.

# Task 8 – Least Privilege Access

# Create DB user:

#     only allowed:
#         SELECT
#         INSERT
#         UPDATE
#     no DROP TABLE permission

# Assignment 3 – Cyber Security Incident Tracking API

# Domain: Security Operations Center (SOC)

# Problem Statement

# A cyber security company wants APIs to:

#     track security incidents
#     assign analysts
#     manage incident severity
#     search attack logs securely

# System must prevent attackers from abusing search functionality.

# Database Requirements

# 1.   Analysts Table

# Column
	

# Type

# analyst_id
	

# INT

# analyst_name
	

# VARCHAR

# skill_level
	

# VARCHAR

# 2. Incidents Table

# Column
	

# Type

# incident_id
	

# INT

# title
	

# VARCHAR

# severity
	

# VARCHAR

# assigned_to
	

# FK

# 3.AttackLogs Table

# Column
	

# Type

# log_id
	

# INT

# source_ip
	

# VARCHAR

# attack_type
	

# VARCHAR

# incident_id
	

# FK

# Assignment Tasks

# Part A – Database Design

# Task 1

# Create all tables with:

#     relationships
#     CHECK constraint on severity:

# LOW, MEDIUM, HIGH

# Task 2

# Insert sample cyber attack logs.

# Part B – SQLAlchemy APIs

# Task 3

# Create API:

# POST /incidents

# Store incident in database.

# Task 4

# Create API:

# GET /incidents/high-severity

# Return all HIGH severity incidents.

# Task 5

# Create API:

# GET /attack-logs/search?ip=10.10.10.1

# Search logs by IP.

# Security Tasks

# Task 6 – Secure Search Implementation

# Students must implement:

#     parameterized queries
#     secure filtering

# Unsafe dynamic SQL not allowed.

# Task 7 – SQL Injection Defense

# Test API with malicious payload:

# 10.10.10.1' OR 1=1 --

# Students must ensure:

#     attack fails
#     only valid records returned

# Task 8 – Secure DB Access Pattern

# Implement:

#     centralized DB session management
#     automatic session closing

# Using:

# yield db
# finally:
#     db.close()