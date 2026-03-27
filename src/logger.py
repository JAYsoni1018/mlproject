import logging
import os
from datetime import datetime

log_path = os.path.join(
    os.getcwd(), "logs", f"app_{datetime.now().strftime('%m-%d-%Y_%H-%M-%S')}.log")
os.makedirs(os.path.dirname(log_path), exist_ok=True)


logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format='[%(asctime)s ] %(lineno)d - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
