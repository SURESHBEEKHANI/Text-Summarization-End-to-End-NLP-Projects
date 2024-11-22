# Importing constants, utility functions, and entity classes
from src.textSummarizer.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.textSummarizer.utils.common import read_yaml, create_directories
from src.textSummarizer.entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
)

class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
        """
        Initializes the ConfigurationManager class by reading configuration and parameter files
        and ensuring the root directories exist.
        """
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # Ensure the root artifacts directory exists
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Reads and parses the data ingestion configuration, and ensures necessary directories exist.
        """
        config = self.config.data_ingestion

        # Create required directories for data ingestion
        create_directories([config.root_dir])

        return DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

    def get_data_validation_config(self) -> DataValidationConfig:
        """
        Reads and parses the data validation configuration, and ensures necessary directories exist.
        """
        config = self.config.data_validation

        # Create required directories for data validation
        create_directories([config.root_dir])

        return DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES,
        )

    def get_data_transformation_config(self) -> DataTransformationConfig:
        """
        Reads and parses the data transformation configuration, and ensures necessary directories exist.
        """
        config = self.config.data_transformation

        # Create required directories for data transformation
        create_directories([config.root_dir])

        return DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            tokenizer_name=config.tokenizer_name
        )
