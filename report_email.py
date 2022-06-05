import os
from datetime import date
import calendar
from reports import generate_report
from emails import generate_email, send_email


# Gets the current date which will be used as the title of the PDF
def get_date():
    today = date.today()

    month = calendar.month_name[today.month]
    day = today.day
    year = today.year

    title = 'Processed Update on {} {}, {}'.format(month, day, year)
    
    return title


# Gets and processes the data from the 'supplier-data/descriptions/' directory which will be used as the main content of the PDF
def get_description_data():
    descriptions_directory = 'supplier-data/descriptions/'
    all_description_contents = []
    description_contents_collection = []
    paragraph = '<br/><br/>'
    
    # Gets the data from each file, converts it to a list and then adds it to another list
    for description in os.listdir(descriptions_directory):
        with open(descriptions_directory + description, 'r') as description_contents:
            i = 0
            description_contents_list = []
            for line in description_contents.readlines():
                # Breaking out of the loop when i = 2 because we only want the name of the fruit and its weight from the files
                if i == 2:
                    break
                description_contents_list.append(line.strip())
                i += 1
        all_description_contents.append(description_contents_list)
          
    # Iterates over the list containing the list of descriptions
    # Converts each list into a dictionary
    # Adds the dictionaries to another list
    for description_data in all_description_contents:
        description_data_dict = {}
        description_data_dict['name'] = description_data[0]
        description_data_dict['weight'] = description_data[1]
        description_contents_collection.append(description_data_dict)
        
    # Iterates over the list containing the dictionaries
    # Adds the content of each dictionary to the 'paragraph' variable which will be used as the body of the PDF
    # Also adds '<br/'> -> (an empty line) between each value so it looks nicely formatted
    for description_content in description_contents_collection:
        paragraph += 'name: {}'.format(description_content['name'])
        paragraph += '<br/>'   
        paragraph += 'weight: {}'.format(description_content['weight'])
        paragraph += '<br/>'
        paragraph += '<br/>'
        
    return paragraph
                
     
                
if __name__ == '__main__':
    generate_report('tmp/processed.pdf', get_date(), get_description_data())
    message = generate_email('automation@example.com', 'username@example.com', 'Upload Completed - Online Fruit Store', 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.','tmp/processed.pdf')
    send_email(message)