from app.config import MAX_FAILED_ATTEMPTS
from app.utils.logger import log_warning

# In-memory employee storage
employees = {}


def register_employee(data):
    employees[data.employee_id] = {
        "employee_id": data.employee_id,
        "name": data.name,
        "department": data.department,
        "age": data.age,
        "failed_attempts": 0,
        "locked": False
    }


def get_employee(emp_id):
    return employees.get(emp_id)


def list_employees(department=None):

    if department:
        return [
            emp for emp in employees.values()
            if emp["department"] == department
        ]

    return list(employees.values())


def process_login_attempt(data):

    emp = employees.get(data.employee_id)

    if not emp:
        return None, "not_found"

    if emp["locked"]:
        return None, "locked"

    if not data.success:
        emp["failed_attempts"] += 1

        if emp["failed_attempts"] >= MAX_FAILED_ATTEMPTS:
            emp["locked"] = True
            log_warning("Account locked due to multiple failed attempts")

    return emp, "ok"


def calculate_risk(emp_id):

    emp = employees.get(emp_id)

    if not emp:
        return None

    score = emp["failed_attempts"] * 25

    if score >= 75:
        level = "HIGH"
    elif 25 <= score <= 50:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "risk_score": score,
        "level": level
    }