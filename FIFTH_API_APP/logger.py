import logging
import os

LOGS_DIR = "logs"
LOG_FILE = os.path.join(LOGS_DIR, "app.log")
os.makedirs(LOGS_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.ERROR,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger("task_api")