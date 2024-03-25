import os
import zipfile
import gdown
from kidneyDiseaseClassifier import logger
from kidneyDiseaseClassifier.utils.common import get_size
from kidneyDiseaseClassifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        """
        Initialize DataIngestion object with the provided configuration.

        Args:
            config (DataIngestionConfig): Configuration object for data ingestion.
        """
        self.config = config

    def download_file(self):
        """Fetch data from a URL.

        Raises:
            Exception: If an error occurs during the download process.
        """
        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)

            logger.info(
                f"Downloading data from {dataset_url} into file {zip_download_dir}")

            file_id = dataset_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?/export=download&id="
            gdown.download(prefix + file_id, zip_download_dir)

            logger.info(
                f"Downloaded data from {dataset_url} into file {zip_download_dir}")

        except Exception as e:
            raise e

    def extract_zip_file(self):
        """Extract a zip file.

            This method extracts the contents of a zip file specified in the configuration
            to the directory specified in the configuration.

            Raises:
                Exception: If an error occurs during the extraction process.
            """
        try:
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)

            with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
                zip_ref.extractall(unzip_path)

            logger.info(f"Extracted zip file into: {unzip_path}")

        except Exception as e:
            logger.error(
                f"Error extracting zip file: {self.config.local_data_file}")
            raise e
