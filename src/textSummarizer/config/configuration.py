# Importing all constants from the `textSummarizer.constants` module.
# This could include configuration settings, file paths, or other fixed values
# used across the text summarization project.
from src.textSummarizer.constants import *

# Importing utility functions from the `textSummarizer.utils.common` module.
# - `read_yaml`: A function to read and parse YAML files, likely used for loading configurations.
# - `create_directories`: A function to create directories on the filesystem,
#   ensuring required folder structures exist for the project.
from src.textSummarizer.utils.common import read_yaml, create_directories
from src.textSummarizer.entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config