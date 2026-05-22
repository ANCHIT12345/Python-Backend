CREATE DATABASE HospitalManagementSystem;
USE HospitalManagementSystem;


CREATE TABLE Patients
(
Patient_ID INT PRIMARY KEY IDENTITY(1,1),
Patient_Name VARCHAR(50) NOT NULL,
Age INT NOT NULL,
Mobile_NO VARCHAR(15)NOT NULL
);

CREATE TABLE Doctors
(
Doctor_ID INT PRIMARY KEY IDENTITY(1,1),
Doctor_Name VARCHAR(50) NOT NULL,
Spetialization VARCHAR(100) NOT NULL
);

CREATE TABLE Appointments
(
Appointmetn_ID INT PRIMARY KEY IDENTITY(1,1),
Patient_ID INT REFERENCES Patients(Patient_ID),
Doctor_ID INT REFERENCES Doctors(Doctor_ID),
Appointment_Date_Time DATETIME
);

INSERT INTO Patients VALUES
('Rahul', 22, '9876543210');

INSERT INTO Doctors VALUES
('Dr Sharma', 'Cardiology');

INSERT INTO Appointments VALUES
(1, 1, '2026-05-10 10:00:00');


SELECT * FROM Patients;
SELECT * FROM Doctors;
SELECT * FROM Appointments;