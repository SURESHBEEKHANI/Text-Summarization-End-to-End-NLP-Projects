from src.textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.textSummarizer.logging import logging
# Now you can log messages


STAGE_NAME = "Data Ingestion stage"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.exception(e)
        raise e
