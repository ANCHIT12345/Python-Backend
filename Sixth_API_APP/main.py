from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import get_db
from curd import create_doctor, create_patient, create_appointment
from models import Doctor, Patient, Appointment

import schemas

