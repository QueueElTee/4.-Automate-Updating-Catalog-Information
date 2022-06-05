import requests
import os

# Takes the processed data from the 'supplier-data/images/' directory and uploads them to a web server

def supplier_image_upload():
    url = 'http://localhost/upload/'
    directory = 'supplier-data/images/'

    for image in os.listdir(directory):
        with open(directory + image, 'rb') as opened:
            requests.post(url, files={'file': opened})
            
            
supplier_image_upload()