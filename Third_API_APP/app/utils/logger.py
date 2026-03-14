import logging 
from app.config import LOG_LEVEL

logging.basicConfig(
    level = getattr(logging, LOG_LEVEL),
    format = "%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("secure_access")

def log_request(endpoint, method, status):
    logger.info(f"(endpoint) | {method} | Status: {status}")

def log_warning(message):
    logger.warning(message)