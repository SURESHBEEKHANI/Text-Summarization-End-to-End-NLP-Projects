# Importing the dataclass decorator from the dataclasses module.
# This decorator simplifies the creation of classes that are primarily used to store data.
from dataclasses import dataclass

# Importing the Path class from the pathlib module.
# Path is used for handling filesystem paths in a way that works across different operating systems.
from pathlib import Path

# Defining a data class for configuration settings related to data ingestion.
# The `frozen=True` argument makes the instances of this class immutable,
# meaning their attributes cannot be modified after creation.
@dataclass(frozen=True)
class DataIngestionConfig:
    # The root directory where all data-related operations will occur.
    root_dir: Path
    
    # The URL from which the data will be sourced.
    source_URL: str
    
    # The local path where the downloaded data file will be stored.
    local_data_file: Path
    
    # The directory where the downloaded data will be extracted/unzipped.
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list
