# Import necessary modules
import os  # Provides functions for interacting with the operating system
import sys  # Provides access to system-specific parameters and functions
import logging  # Provides a flexible framework for logging messages

# Define the logging format string with placeholders for specific details
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
# Explanation of the format string:
# %(asctime)s: Logs the timestamp of the log message
# %(levelname)s: Logs the severity level of the log (e.g., INFO, ERROR, etc.)
# %(module)s: Logs the name of the module (Python file) where the log was generated
# %(message)s: Logs the actual log message

# Define the directory where log files will be stored
log_dir = "logs"
# Define the full path of the log file, combining the directory and filename
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create the directory to store log files if it does not already exist
os.makedirs(log_dir, exist_ok=True)
# exist_ok=True ensures that no error is raised if the directory already exists

# Configure the logging settings
logging.basicConfig(
    level=logging.INFO,  # Set the default logging level to INFO
    format=logging_str,  # Use the custom format string for log messages
    handlers=[  # Define the log message handlers
        # Handler to log messages to a file
        logging.FileHandler(log_filepath),
        # Handler to log messages to the console (standard output)
        logging.StreamHandler(sys.stdout)
    ]
)

# Create a logger instance named 'textSummarizerLogger'
logger = logging.getLogger("textSummarizerLogger")
# This logger will be used throughout the code to log messages with the specified settings
