#!/user.bin.env python3

"""
Opening Docstring

GitHub URL: https://github.com/kasnyd/DataValidation
"""

import re  # For finding and creating formatting rules/ errors
import csv  # Allows Import and Export of .csv files
from datetime import datetime  # Allows specifications on the date and time

__author__ = 'Rivar Yoder | Kaeden Snyder'
__version__ = '1.0'
__date__ = '4/22/2024'
__status__ = 'Development'

DASH_LENGTH = 40  # Used in formatting


def validate_id(id):
    """

    :param id:
    :return:
    """
    regex = "^\\d+$"
    if re.compile(regex).match(id[0]):
        return ""
    else:
        return "I"


def validate_name(name):
    """

    :param name:
    :return:
    """

    names = name.split(",")
    if len(names) == 2:
        return ""
    else:
        return "N"


def validate_email(email):
    """
    Receives the email from the current data string, checks that it is in the standard format for email addresses

    ChatGPT referenced to explain regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+/.[A-Z|a-z]{2,7}\b
    https://chat.openai.com/share/4b3e4eb8-cade-4e58-8727-cf0d9ff6d495
        \b - The start of the email
        [A-Za-z0-9._%+-] - Represents the characters that can be used in an email username
        @ - Ensures '@' is present
        [A-Za-z0-9.-] - Represents the text that can be used in the domain name, does not include top level domain
        /. - Ensures the '.' is present
        [A-Z|a-z]{2,7} - 2 to 7 upper or lowercase characters that make up the top level domain
        \b - End of the email
        + - Utilized to add all arguments together

    :param email:
    :return:
    """

    # establishes email format (See docstring above for detail)
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.fullmatch(regex, email):  # Compares the email to the format rules
        return ''  # Keeps error_string empty if all is good
    else:
        return 'E'  # Pushed to error_string, will be displayed


def validate_phone(phone):
    """
    Receives the phone number from the current data string, checks that it is in the standard format for phone numbers

    ChatGPT referenced to explain regex = r'^/d{3}-/d{3}-/d{4}$'
    https://chat.openai.com/share/4b3e4eb8-cade-4e58-8727-cf0d9ff6d495
        r'^ - Beginning of string
        /d{3} (Used twice) - Any single digit can be used to fill in each of the 3 characters
        '-' - Hyphen as separate
        /d{4} - Same as /d{3} but with 4 digits
        $' - end of the string

    :param phone:
    :return:
    """

    # establishes phone number format (See docstring above for detail)
    regex = r'^\d{3}-\d{3}-\d{4}$'
    if re.fullmatch(regex, phone):
        return ''  # Keeps error_string empty if all is good
    else:
        return 'P'  # Pushed to error_string, will be displayed


def validate_date(date):
    date_format = "%m/%d/%Y"
    try:
        datetime.strptime(date, date_format)
        return ''
    except ValueError:
        return 'D'


def validate_time(time):
    time_format = "%H:%M"
    try:
        datetime.strptime(time, time_format)
        return ''
    except ValueError:
        return 'T'


def process_file():
    try: # opens DataInput to be read, ValidData to be written, and Invalid Data to be written
        with open('DataInput.csv', 'r', newline='') as input_file, \
                open('ValidData.csv', 'w', newline='') as valid_file, \
                open('InvalidData.csv', 'w', newline='') as invalid_file:

            reader = csv.reader(input_file, delimiter='|')  # Makes reader for DataInput, pipe delimited
            valid_writer = csv.writer(valid_file, delimiter=',')
            invalid_writer = csv.writer(invalid_file, delimiter='|')  # Makes reader for InvalidData, pipe delimited

            input_counter = 0  # Will be used to separate all the inputs and number them to be displayed

            for row in reader:
                error_string = ""
                data_count = len(row)
                input_counter += 1

                print('Input', input_counter, ':')

                if data_count == 6:
                    error_string += validate_id(row[0])
                    error_string += validate_name(row[1])
                    error_string += validate_email(row[2])
                    error_string += validate_phone(row[3])
                    error_string += validate_date(row[4])
                    error_string += validate_time(row[5])
                else:
                    error_string = "C"

                print(error_string)
                print()

                if error_string == '':
                    last_name, first_name = row[1].split(',')
                    row[1] = f'{first_name} {last_name}'
                    row[3] = re.sub('-', '.', row[3])
                    row[4] = re.sub('/', '-', row[4])
                    valid_writer.writerow(row)
                else:
                    row.insert(0, error_string)
                    invalid_writer.writerow(row)

            print('=' * DASH_LENGTH)
            print(f'{'Read Complete': >25}')
            print('=' * DASH_LENGTH)

    except OSError:
        print('Unable to access files')


def display_report():
    """

    :return:
    """

    print('=' * DASH_LENGTH)
    print(f'{'Error Index': >25}')
    print('=' * DASH_LENGTH)

    print('C: Not all data is present')
    print('I: ID is not an integer')
    print('N: Name is not in FIRSTNAME, LASTNAME format')
    print('E: Email is not in proper email format or the .edu extension')
    print('D: Date is not in MM/DD/YYY format')
    print('T: Time is not in HH:MM military format')
    print()

    print('=' * DASH_LENGTH)
    print(f'{'Errors Found': >25}')
    print('=' * DASH_LENGTH)

    try:
        process_file()
    except OSError:
        print('Cannot run process_file')


if __name__ == '__main__':
    display_report()
