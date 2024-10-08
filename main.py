#!/user.bin.env python3

"""
Opening Docstring

All data is generated by ChatGPT:
https://chat.openai.com/share/1ba4a8aa-70ba-4126-a157-40381f305bda

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


def validate_id(ident):
    """

    :param ident:
    :return:
    """
    regex = "^\\d+$"
    if re.compile(regex).match(ident[0]):
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
    """
    Program opens DataInput, ValidData, and InvalidData- all CSV files. DataInput and InvalidData are both pipe
    delimited, ValidData is comma delimited.

    A For loop is used to iterate through each line of DataInput to validate the id, name, email, phone, date, and time
    If the data does not have all these elements or has to many, a count error is given instead. The errors are
    displayed to the user.

    An if-else statement sorts each row into ValidData and InvalidData, if it is Valid the first name and last names are
    swapped, the '-' in phone is replaced with '.', and '/' in date is replaced with '-' for the sake of format changes.
    Invalid data is not altered and will be written to InvalidData.

    ChatGPT used as reference for reformatting names and writing cvs files:
    https://chat.openai.com/share/8ac2ffbf-e9b8-415a-a7eb-c5dde0b13892
    :return:
    """
    try:  # opens DataInput to be read, ValidData to be written, and Invalid Data to be written
        with open('DataInput.csv', 'r', newline='') as input_file, \
                open('ValidData.csv', 'w', newline='') as valid_file, \
                open('InvalidData.csv', 'w', newline='') as invalid_file:

            reader = csv.reader(input_file, delimiter='|')  # Makes reader for DataInput, pipe delimited
            valid_writer = csv.writer(valid_file, delimiter=',')
            invalid_writer = csv.writer(invalid_file, delimiter='|')  # Makes reader for InvalidData, pipe delimited

            input_counter = 0  # Tracks how many total data inputs there are
            valid_count = 0  # Keeps track of how many are valid
            invalid_count = 0  # Keeps track of how many are invalid

            for row in reader:  # Iterates through each line of DataInput
                error_string = ""  # Empties error_string each time a new line is checked
                data_count = len(row)  # Checks how many strings there are in the line
                input_counter += 1  # Tracks how many times there is an interation

                if data_count == 6:  # Only runs if there are six strings in the row
                    error_string += validate_id(row[0])  # Checks the ID
                    error_string += validate_name(row[1])  # Checks the name
                    error_string += validate_email(row[2])  # Checks the email
                    error_string += validate_phone(row[3])  # Checks the phone number
                    error_string += validate_date(row[4])  # Checks the date
                    error_string += validate_time(row[5])  # Checks the time
                else:  # Runs if there are more or less strings to check than necessary
                    error_string = "C"  # Counter error

                if error_string == '':
                    valid_count += 1  # Adds to be displayed later
                    last_name, first_name = row[1].split(',')  # Splits the name by the comma
                    row[1] = f'{first_name} {last_name}'  # Flips first_name and last name
                    row[3] = re.sub('-', '.', row[3])  # Replaces '-' with '.' in phone number
                    row[4] = re.sub('/', '-', row[4])  # Replaces '/' with '-' in date
                    valid_writer.writerow(row)  # Writes row to ValidData
                else:
                    invalid_count += 1  # Adds to be displayed later
                    row.insert(0, error_string)  # Puts the error codes at the beginning of row
                    invalid_writer.writerow(row)  # Writes row to InvalidData

        display_report(input_counter, valid_count, invalid_count)

    except OSError:
        print('Unable to access files')  # Error message for if the files do not open


def display_report(input_counter, valid_count, invalid_count):
    """
    Opening message for the user

    Displays each error code and the meaning behind each code
    Codes:
        C - Count
        I - ID
        N - Name
        E - Email
        P - Phone
        D - Date
        T - Time

    Message to separate the Index from the report
    Runs process_file

    :return:
    """

    # User Interface
    print('=' * DASH_LENGTH)
    print(f'{'Read Complete': >25}')
    print('=' * DASH_LENGTH)

    print('Total Input Checked:', input_counter)
    print('Total Valid Input:  ', valid_count)
    print('Total Invalid Input:', invalid_count)

    print('=' * DASH_LENGTH)
    print(f'{'Error Index': >25}')
    print('=' * DASH_LENGTH)

    print('C: Not all data is present')
    print('I: ID not an integer')
    print('N: Name not in two name format')
    print('E: Email not in email format or .edu')
    print('D: Date not in MM/DD/YYY format')
    print('T: Time not in HH:MM military format')

    print('=' * DASH_LENGTH)
    print(f'{'Goodbye! :)': >25}')
    print('=' * DASH_LENGTH)


if __name__ == '__main__':
    process_file()
