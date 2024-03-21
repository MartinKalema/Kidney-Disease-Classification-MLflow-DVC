import sys
import os
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs" # Directory where the logs are stored
log_file_path = os.path.join(log_dir, "logs.log") # Path to log file
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str, # Specifies the format of the log messages
    handlers=[
        logging.FileHandler(log_file_path), # Log messages to a file at a specific path
        logging.StreamHandler(sys.stdout) # Log messages to the console
    ]
)

logger = logging.getLogger('kidneyDiseaseClassifierLogger') # Creates a logger object