#!/user.bin.env python3

"""
Opening Docstring

GitHub URL: https://github.com/kasnyd/DataValidation
"""

#  Insert Imports As Needed

import re
import csv
from datetime import datetime

__author__ = 'Rivar Yoder | Kaeden Snyder'
__version__ = '1.0'
__date__ = '4/22/2024'
__status__ = 'Development'


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


# Validate Name


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

    :param email:
    :return:
    """

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.fullmatch(regex, email):
        return ''
    else:
        return 'E'


def validate_phone(phone):
    """

    :param phone:
    :return:
    """

    regex = r'^\d{3}-\d{3}-\d{4}$'
    if re.fullmatch(regex, phone):
        return ''
    else:
        return 'P'


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
    DASH_LENGTH = 40

    try:
        with open('DataInput.csv', 'r', newline='') as input_file, \
                open('ValidData', 'w', newline='') as valid_file, \
                open('InvalidData.csv', 'w', newline='') as invalid_file:

            reader = csv.reader(input_file, delimiter='|')
            valid_writer = csv.reader(valid_file, delimiter=',')
            invalid_writer = csv.writer(invalid_file, delimiter='|')

            input_counter = 0

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

                #  if error_string == ' ':
                #  valid_file.write(row)
                #  else:
                #  invalid_file.write(row)

            print('=' * DASH_LENGTH)
            print(f'{'Read Complete': >25}')
            print('=' * DASH_LENGTH)

    except OSError:
        print('Unable to access files')


def display_report():
    """

    :return:
    """

    DASH_LENGTH = 40

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
