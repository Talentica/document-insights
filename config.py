import os

class BaseConfig:
    #Add all base level configurations here.
    SECRET_KEY = os.getenv('SECRET_KEY', 'this_is_my_secret_key')
    ENVIRONMENT = "DEV" # DEV | PROD