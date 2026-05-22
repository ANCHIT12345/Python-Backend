from sqlalchemy import Column, Integer, String, ForeignKey, DateTime # pyright: ignore[reportMissingImports]
from sqlalchemy.orm import relationship # pyright: ignore[reportMissingImports]

from database import Base


class Patient(Base):

    __tablename__ = "patients"

    patient_id = Column(Integer, primary_key=True, index=True)

    patient_name = Column(String, nullable=False)

    age = Column(Integer, nullable=False)

    mobile = Column(String, nullable=False)

    appointments = relationship(
        "Appointment",
        back_populates="patient"
    )


class Doctor(Base):

    __tablename__ = "doctors"

    doctor_id = Column(Integer, primary_key=True, index=True)

    doctor_name = Column(String, nullable=False)

    specialization = Column(String, nullable=False)

    appointments = relationship(
        "Appointment",
        back_populates="doctor"
    )


class Appointment(Base):

    __tablename__ = "appointments"

    appointment_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    patient_id = Column(
        Integer,
        ForeignKey("patients.patient_id"),
        nullable=False
    )

    doctor_id = Column(
        Integer,
        ForeignKey("doctors.doctor_id"),
        nullable=False
    )

    appointment_date = Column(
        DateTime,
        nullable=False
    )

    patient = relationship(
        "Patient",
        back_populates="appointments"
    )

    doctor = relationship(
        "Doctor",
        back_populates="appointments"
    )