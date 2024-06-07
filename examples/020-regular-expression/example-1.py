import re

def is_valid_email(email):
    
    # Define the regular expression pattern for a basic email validation
    email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    
    # Check if the input string matches the pattern
    return bool(email_pattern.match(email))

email_address = "user@example.com"

if is_valid_email(email_address):
    print(f"{email_address} is a valid email address.")
else:
    print(f"{email_address} is not a valid email address.")