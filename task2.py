# Flow 29
# Task 2

import re
def validate_email(email):
    reg = re.compile("[a-z]+\@(hr|it|fin|mkt|ops)\.company\.com")
    #Don't see reason why not to accumulate first name initial and last name all together
    m = reg.match(email)
    if m != None:
        print(f'The email {email} is valid')
        return True
    else:
        print(f'The email {email} is invalid')
        return False

def get_department(email):
    reg = re.compile("[a-z]+\@(hr|it|fin|mkt|ops)\.company\.com")
    m = reg.match(email)
    if m != None:
        print(m.group(1))
    else:
        return None

def categorize_emails(email_list):
    dictionary = {}
    reg = re.compile("[a-z]+\@(hr|it|fin|mkt|ops)\.company\.com")
    for email in email_list:
        m = reg.match(email)
        if m != None:
            department = m.group(1)
            if department == 'hr':
                dictionary['hr'] = email
            elif department == 'it':
                dictionary['it'] = email
            elif department == 'fin':
                dictionary['fin'] = email
            elif department == 'mkt':
                dictionary['mkt'] = email
            elif department == 'ops':
                dictionary['ops'] = email
    return dictionary


email = 'jdoe@fin.company.com'
email_list = ['jdoe@fin.company.com', 'jdoe@hr.company.com', 'RandomNonsense']
validate_email(email)
get_department(email)
dictionary = categorize_emails(email_list)
print(dictionary)
