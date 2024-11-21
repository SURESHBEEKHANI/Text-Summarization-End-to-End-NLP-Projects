# Importing the 'os' module for operating system interactions such as handling file paths,
# environment variables, and directory manipulations.
import os
# Importing 'BoxValueError' from the 'box.exceptions' module to handle errors related to 'Box' objects.
# 'Box' is a dictionary-like object that supports attribute-style access.
from box.exceptions import BoxValueError

# Importing the 'yaml' library to parse and generate YAML files.
# YAML is commonly used for configuration files due to its simplicity and readability.
import yaml

# Importing the 'logging' module from the custom 'textSummarizer' package.
# This is likely a pre-configured logger used to track and debug application behavior.
from src.textSummarizer.logging import logging

# Importing 'ensure_annotations' from the 'ensure' library to enforce the use of type annotations.
# This ensures that functions are properly annotated, promoting type safety and code clarity.
from ensure import ensure_annotations

# Importing 'ConfigBox' from the 'box' library.
# 'ConfigBox' is a specialized data structure that combines dictionary functionality with attribute-style access.
# It's commonly used to simplify configuration handling in Python applications.
from box import ConfigBox

# Importing 'Path' from the 'pathlib' module.
# The 'Path' class provides a modern, object-oriented approach to file and directory path management.
# It's a cleaner and more robust alternative to using 'os.path'.
from pathlib import Path

# Importing 'Any' from the 'typing' module.
# 'Any' is used for type annotations when the type of a variable, function parameter, or return value can be anything.
from typing import Any


##late stared Works 

# Importing the 'ensure_annotations' decorator to enforce type annotations for this function.
# This ensures the function parameters and return types adhere to the specified types at runtime.
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.

    Args:
        path_to_yaml (Path): Path object representing the path to the YAML file.

    Raises:
        ValueError: Raised if the YAML file is empty or cannot be loaded into a ConfigBox.
        Exception: Raised for any other exceptions during file handling or parsing.

    Returns:
        ConfigBox: The parsed content of the YAML file, wrapped in a ConfigBox for easy access.
    """
    try:
        # Opening the YAML file specified by 'path_to_yaml'.
        with open(path_to_yaml) as yaml_file:
            # Using 'yaml.safe_load' to safely parse the YAML content into a Python dictionary.
            content = yaml.safe_load(yaml_file)
            
            # Logging a success message indicating the YAML file was loaded correctly.
            logging.info(f"yaml file: {path_to_yaml} loaded successfully")
            
            # Returning the content as a ConfigBox, enabling attribute-style access to the parsed data.
            return ConfigBox(content)
    except BoxValueError:
        # Handling the specific case where the YAML file is empty or has invalid content for a ConfigBox.
        raise ValueError("yaml file is empty")
    except Exception as e:
        # Catching any other exceptions that occur during file handling or parsing, and re-raising them.
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates a list of directories.

    Args:
        path_to_directories (list): A list of directory paths to create.
        verbose (bool, optional): If True, logs a message for each created directory. Defaults to True.
    """
    for path in path_to_directories:
        # Create the directory at the specified path. 'exist_ok=True' ensures no error is raised if the directory exists.
        os.makedirs(path, exist_ok=True)
        
        # If verbose is True, log a success message indicating the directory was created.
        if verbose:
            logging.info(f"created directory at: {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Returns the size of a file in KB.

    Args:
        path (Path): Path to the file whose size is to be determined.

    Returns:
        str: File size in KB as a formatted string.
    """
    # Calculate the size of the file in bytes, then convert to kilobytes (KB) by dividing by 1024.
    size_in_kb = round(os.path.getsize(path) / 1024)
    
    # Return the size as a string formatted to approximate value in KB.
    return f"~ {size_in_kb} KB"

