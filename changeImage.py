import os
from PIL import Image

# Converts the format of images in the 'supplier-data/images/' directory from tiff to jpeg
# Also changes the resolution of the images from '3000 x 2000' to '600 x 400' 
# Then deletes the original .tiff formats

def change_image():
    directory = 'supplier-data/images/'

    for image in os.listdir(directory):
        tiff_format = directory + image
        im = Image.open(tiff_format)
        im.convert('RGB').resize((600, 400)).save(tiff_format.strip('.tiff') + '.jpeg')
        os.remove(tiff_format)
        
        
change_image()