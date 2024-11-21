# Import necessary modules
import os  # Provides functions for interacting with the operating system
from pathlib import Path  # Provides object-oriented filesystem paths
import logging  # Provides functionality for logging messages

# Configure the logging system to log messages at INFO level and with a specific format
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Define the project name
project_name = "textSummarizer"

# List of file paths that need to be checked or created
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",  # Corrected spelling from "conponents"
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]

# Loop through each file path in the list to check and create directories or files as necessary
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert the file path to a Path object
    filedir, filename = os.path.split(filepath)  # Split the file path into directory and file name

    # If the directory does not exist, create it
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Create the directory if it doesn't exist
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    # If the file does not exist or is empty, create an empty file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass  # Open the file in write mode, but do not write anything to it (creates an empty file)
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")  # Log a message if the file already exists and is not empty
