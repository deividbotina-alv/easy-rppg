import logging
import os
from datetime import datetime

"""
Handle logs
"""

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(),"logs", LOG_FILE)
os.makedirs(log_path, exist_ok = True)

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)

# if __name__=="__main__":
#     " Example of Logging"
#     logging.info("Logging has started")