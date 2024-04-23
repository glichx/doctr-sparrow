from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    huggingface_key: str = os.environ.get("huggingface_key")
    sparrow_key: str = os.environ.get("sparrow_key")
    secure_key: str = os.environ.get("secure_key")
    dataset_name: str = "katanaml-org/invoices-donut-data-v1"
    ocr_stats_file: str = "data/ocr_stats.json"


settings = Settings()