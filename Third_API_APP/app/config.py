import os
from dotenv import load_dotenv

load_dotenv()

REQUIRED_ENV_VARS = [
    "APP_NAME",
    "APP_VERSION",
    "APP_ENV",
    "MAX_FAILED_ATTEMPTS",
    "LOG_LEVEL"
]

for var in REQUIRED_ENV_VARS:
    if os.getenv(var) is None:
        raise EnvironmentError(f"Missing required environment variable: {var}")

APP_NAME = os.getenv("APP_NAME")
APP_VERSION = os.getenv("APP_VERSION")
APP_ENV = os.getenv("APP_ENV")

MAX_FAILED_ATTEMPTS = int(os.getenv("MAX_FAILED_ATTEMPTS"))
LOG_LEVEL = os.getenv("LOG_LEVEL")

if APP_ENV == "prod":
    LOG_LEVEL = "Warning"