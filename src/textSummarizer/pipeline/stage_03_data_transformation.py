from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.conponents.data_transformation import DataTransformation
from src.textSummarizer.logging import logging


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()