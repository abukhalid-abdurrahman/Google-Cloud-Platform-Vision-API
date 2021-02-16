import os, io
from google.cloud import vision

def GetImage(filename, folderPath):
    with io.open(os.path.join(folderPath, filename), 'rb') as image_file:
        content = image_file.read()
        image = vision.Image(content=content)
        return image