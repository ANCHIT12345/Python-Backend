Please follow below Project Structure for assignment:

app/

├── main.py

├── services/

│ └── logic_service.py

├── utils/

│ ├── validators.py

│ └── error_handler.py

└── config.py

1. Health Check with Computation

Create GET /api/health that:

    calculates server uptime in seconds
    returns:

{

"status": "UP",

"uptime": 345,

"message": "Service running normally"

}

Uptime logic must be in services/logic_service.py

2. Dynamic About API

Create GET /api/about that:

    reads app name & version from config.py
    adds runtime info (Python version)

{

"app": "Secure API",

"version": "1.0",

"python": "3.11"

}

3. Input-Based Logic API

Create GET /api/calculate with query params:

    a
    b
    operation (add, sub, mul, div)

🔹 Return calculation result
🔹 Reject invalid operations

4. Create a validator function:

validate_operation(operation: str)

    must be reusable
    must raise exception on invalid input

used by multiple endpoints

5.Conditional Response Logic

Create GET /api/risk-score?age=30&failed_logins=5

Rules:

    risk score = age + (failed_logins × 10)
    if score > 80 → HIGH
    else → LOW

Return:

{

"riskScore": 80,

"level": "HIGH"

}

6. Reusable Response Formatter

Create a function:

build_response(data, message)

Used by all endpoints.

7. Centralized Exception Handler

Implement a global exception handler that:

    catches unhandled errors
    returns:

{

"error": "Internal server error"

}

⚠️ No stack trace exposure

7. Virtual Environment Setup

Run app only inside a virtual environment.

📌 Include:

    requirements.txt
    FastAPI
    Uvicorn

8. Dependency Isolation Test

Install one extra package only inside venv
Prove app fails outside venv.
