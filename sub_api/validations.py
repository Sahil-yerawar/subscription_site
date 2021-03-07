import re

def email_validate(email_st):
    if re.match('[a-zA-Z0-9.!#$%&\'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*',email_st):
        return True
    else:
        return False