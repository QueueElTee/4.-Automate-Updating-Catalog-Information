from email.message import EmailMessage
from emails import send_email
import shutil, psutil, socket


sender = 'automation@example.com'
recipient = 'username@example.com'
body = 'Please check your system and resolve the issue as soon as possible.'


# Generates an email
def generate_error_report(sender, recipient, error, body):
    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = error
    message.set_content(body)
        
    return message


# Checks several statistics about the system
# If any issue is detected, an email will be sent with an appropriate subject
def check_system_stats():
    cpu_usage = psutil.cpu_percent(0.5)
    
    available_disk_space = (shutil.disk_usage('/').free / shutil.disk_usage('/').total) * 100
    
    total_memory = psutil.virtual_memory().total / (1024 * 1024)
    utilized_memory = psutil.virtual_memory().used / (1024 * 1024)
    available_memory = total_memory - utilized_memory
    
    local_host = socket.gethostbyname('localhost')
        
    if cpu_usage > 80:
        error = 'Error - CPU usage is over 80%'
        message = generate_error_report(sender, recipient, error, body)
        send_email(message)
        
    if available_disk_space < 20:
        error = 'Error - Available disk space is less than 20%'
        message = generate_error_report(sender, recipient, error, body)
        send_email(message)

    if available_memory < 500:
        error = 'Error - Available memory is less than 500MB'
        message = generate_error_report(sender, recipient, error, body)
        send_email(message)
        
    if local_host != '127.0.0.1':
        error = 'Error - localhost cannot be resolved to 127.0.0.1'
        message = generate_error_report(sender, recipient, error, body)
        send_email(message)
        


check_system_stats()