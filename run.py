import os
import json
import requests

description_directory = 'supplier-data/descriptions/'
image_directory = 'supplier-data/images/'

list_of_descriptions = []
image_names = []
list_of_descriptions_json = []

# Processes the text files
# Gets the individual contents of a file and adds them to a list line by line
# Adds each file that has been converted into a list to another list
def process_txt_files():
    for file in os.listdir(description_directory):
        full_path = description_directory + file
        with open(full_path, 'r') as description:
            single_description_contents = []
            for line in description.readlines():
                single_description_contents.append(line.strip())
        list_of_descriptions.append(single_description_contents)
    

# Gets the names of all the images in the 'supplier-data/images/' directory and adds them to a list
def get_image_names():
    for image in os.listdir(image_directory):
        image_names.append(image)
        

# Creates dictionaries based on each description
# Adds the image name generated from the previous function as part of the dictionary's fields
# Converts each dictionary to JSON and adds it to a list    
def generate_json():
    i = 0
    for description in list_of_descriptions:
        description_dict =  {}
        description_dict['name'] = description[0]
        description_dict['weight'] = int(description[1].strip(' lbs'))
        description_dict['description'] = description[2]
        description_dict['image_name'] = image_names[i]
        list_of_descriptions_json.append(json.dumps(description_dict))
        i += 1
     

# Iterates over the list containing the JSON structures and posts the content to a web server   
def post_to_web_service():
    url = 'http://[linux-instance-external-IP]/fruits'
    for description in list_of_descriptions_json:
        requests.post(url, data=description)
        
        
        
process_txt_files()
get_image_names()
generate_json()
post_to_web_service()