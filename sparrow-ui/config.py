import os


class Settings():
    sparrow_key = os.environ.get("sparrow_key")


settings = Settings()