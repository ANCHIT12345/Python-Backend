import sys
from fastapi import FastAPI, Query
from app.services.logic_service import (
    get_uptime_seconds,
    calculate,
    calculate_risk
)
from app.utils.validators import validate_operation
from app.utils.error_handler import global_exception_handler
from app.config import APP_NAME, APP_VERSION


app = FastAPI()
app.add_exception_handler(Exception, global_exception_handler)

@app.get("/api/health")
def health():
    return{ 
           "status": "UP",
           "uptime": get_uptime_seconds(),
           "message": "Service running normally"
           }

@app.get("/api/about")
def about():
    return {
        "app_name": APP_NAME,
        "version": APP_VERSION,
        "python": sys.version.split()[0]
    }
    
@app.get("/api/calculate")
def calculate_api(
    a: int = Query(...),
    b: int = Query(...),
    operation: str = Query(...)
):
    validate_operation(operation)
    result = calculate(a, b, operation)
    return {
        "operation": operation,
        "operands": [a, b],
        "result": result
    }  
    
@app.get("/api/risk-score")
def risk_score(age: int, failed_logins: int):
    score, level = calculate_risk(age, failed_logins)
    return{
        "riskScore": score,
        "level": level
    }