import os
from google.cloud import vision
import configs

def CreateApplication():
    os.environ[configs.CREDENTIALS_KEY_NAME] = configs.KEY_FILE_NAME
    client = vision.ImageAnnotatorClient()
    return client