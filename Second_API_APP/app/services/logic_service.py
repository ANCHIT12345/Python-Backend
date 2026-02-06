import time

START_TIME = time.time()

def get_uptime_seconds():
    return int(time.time() - START_TIME)

def calculate(a: int, b: int, operation: str):
    if operation == "add":
        return a + b
    if operation == "sub":
        return a - b
    if operation == "mul":
        return a * b
    if operation == "div":
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b
    
def calculate_risk(age: int, failed_logins: int):
    score  = age + (failed_logins * 10)
    level = "HIGH" if  score > 80 else "LOW"
    return score, level