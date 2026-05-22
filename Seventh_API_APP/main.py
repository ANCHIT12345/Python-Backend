# main.py
from fastapi import FastAPI
import models
from database import engine, SessionLocal
from auth import get_password_hash
from routes import banking_routes, hr_routes, incidents_routes

# Initialize DB tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Secure Banking, HR, and SOC APIs")

app.include_router(banking_routes.router)
app.include_router(hr_routes.router)
app.include_router(incidents_routes.router)

@app.on_event("startup")
def seed_database():
    """Seeds the DB with test users and data if it's empty."""
    db = SessionLocal()
    if not db.query(models.User).first():
        # Seed Users
        users = [
            models.User(username="rahul", password_hash=get_password_hash("rahul123"), role="Customer", team="None"),
            models.User(username="alice", password_hash=get_password_hash("password"), role="Employee", team="None"),
            models.User(username="bob", password_hash=get_password_hash("password"), role="HR", team="None"),
            models.User(username="charlie", password_hash=get_password_hash("password"), role="Admin", team="SOC-Core"),
            models.User(username="dave", password_hash=get_password_hash("password"), role="Analyst", team="SOC-T1"),
            models.User(username="eve", password_hash=get_password_hash("password"), role="Manager", team="SOC-T2"),
        ]
        db.add_all(users)
        db.commit()

        # Seed Banking Data for Rahul
        rahul = db.query(models.User).filter(models.User.username == "rahul").first()
        db.add(models.BankingProfile(user_id=rahul.id, account_number="123456789", balance=5432.00))
        db.add(models.Transaction(user_id=rahul.id, amount=-50.00, description="Groceries"))

        # Seed HR Data
        alice = db.query(models.User).filter(models.User.username == "alice").first()
        db.add(models.EmployeeData(user_id=alice.id, full_name="Alice Smith", department="Engineering"))

        # Seed SOC Data
        db.add(models.Incident(title="Suspicious Login Detected", status="Open", severity="High"))
        db.add(models.AuditLog(action="System Startup", username="system"))
        
        db.commit()
    db.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
    
    
# Assignment 1 – Secure Online Banking API

# Domain: Banking System

# Problem Statement

# A bank wants to secure its internal APIs using JWT authentication.

# Users should:

#     Login securely
#     Receive JWT token
#     Access protected account APIs

# The system must:

#     Reject invalid tokens
#     Reject expired tokens
#     Allow only authenticated users

# Functional Requirements

# User Roles

#     Customer → View account details
#     Employee → Internal support access

# APIs to Build

#     Login API

# Endpoint:
# POST /login

# Input:

# {
#   "username": "rahul",
#   "password": "rahul123"
# }

# Requirements:

#     Validate credentials
#     Generate JWT token
#     Token expiry should be 15 minutes

#     Protected Account API

# Endpoint:
# GET /account/profile

# Requirements:

#     Require Authorization header
#     Validate JWT token
#     Return customer account details

#     Transaction API

# Endpoint:
# GET /transactions

# Requirements:

#     Accessible only with valid JWT token
#     Return fake transaction history

# Security Requirements

#     Token Validation
#     Reject:

#     Malformed tokens
#     Fake tokens
#     Expired tokens

#     Authorization Header Validation
#     Reject requests if Authorization header is missing.
#     Expiration Check
#     Students must:

#     Set token expiration
#     Demonstrate expired token behavior

# Testing Scenarios

#     Valid token → Success
#     Missing token → 401 Unauthorized
#     Invalid token → 401 Unauthorized
#     Expired token → 401 Unauthorized

# Learning Outcome

# Students learn:

#     JWT generation
#     Token validation
#     Protected APIs
#     Stateless authentication
#     Authorization header handling

# Assignment 2 – Company HR Management System (RBAC)

# Domain: Enterprise HR Portal

# Problem Statement

# A company wants role-based access control (RBAC) for HR APIs.

# Different users should have different permissions.

# User Roles

#     Employee → View own profile
#     HR → Manage employees
#     Admin → Full access

# APIs to Build

#     Login API

# Endpoint:
# POST /login

# Requirements:

#     Generate JWT token
#     Include username and role inside token payload

#     Employee Dashboard API

# Endpoint:
# GET /employee/dashboard

# Accessible by:

#     Employee
#     HR
#     Admin

#     HR Management API

# Endpoint:
# GET /hr/employees

# Accessible only by:

#     HR
#     Admin

#     Admin API

# Endpoint:
# DELETE /admin/remove-employee/{id}

# Accessible only by:

#     Admin

# Security Requirements

#     RBAC Dependency
#     Create reusable dependency:

# require_role()

#     Role Validation
#     Reject unauthorized access using:

# 403 Forbidden

#     Token Payload Validation
#     Ensure token contains:

#     Username
#     Role

# Testing Scenarios

#     Employee accessing Admin API → Forbidden
#     HR accessing HR API → Allowed
#     Admin accessing all APIs → Allowed

# Learning Outcome

# Students learn:

#     RBAC implementation
#     Authorization dependencies
#     Role validation
#     Access restriction
#     Enterprise API security

# Assignment 3 – Cyber Security Incident Response API

# Domain: SOC (Security Operations Center)

# Problem Statement

# A cyber security company wants secure APIs for:

#     Security analysts
#     SOC managers
#     Incident administrators

# The system must:

#     Authenticate users
#     Authorize users based on role
#     Protect incident APIs

# Roles

#     Analyst → View incidents
#     Manager → Assign incidents
#     Admin → Close incidents

# APIs to Build

#     Login API

# Endpoint:
# POST /login

# Requirements:

#     Generate JWT token
#     Include username, role, and team inside token payload

#     Incident List API

# Endpoint:
# GET /incidents

# Accessible by:

#     Analyst
#     Manager
#     Admin

#     Assign Incident API

# Endpoint:
# PUT /incidents/assign/{id}

# Accessible only by:

#     Manager
#     Admin

#     Close Incident API

# Endpoint:
# POST /incidents/close/{id}

# Accessible only by:

#     Admin

#     Security Audit API

# Endpoint:
# GET /security/audit-logs

# Accessible only by:

#     Admin

# Security Requirements

#     JWT Validation Dependency
#     Protect all incident APIs using token validation dependency.
#     Role-Based Access
#     Implement:

#     Analyst restrictions
#     Manager permissions
#     Admin full access

#     Token Tampering Test
#     Students must test:

#     Modified token payload
#     Invalid signature

# Expected Result:

# 401 Unauthorized

#     Secure Error Handling
#     Do not expose:

#     Stack traces
#     Secret keys
#     Internal validation details

# Bonus Challenge

# Implement token blacklist/logout functionality.