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


# Validate ID
def validate_id(id):
    """

    :param id:
    :return:
    """
    regex = "^\\d+$"
    if re.compile(regex).match(id[0]):
        return "(PASS)"  # Change to '' after testing
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
        return "(PASS)"  # Change to '' after testing
    else:
        return "N"


def validate_email(email):
    """

    :param email:
    :return:
    """

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.fullmatch(regex, email):
        return '(PASS)'  # Change to '' after testing
    else:
        return 'E'


def validate_phone(phone):
    """

    :param phone:
    :return:
    """

    regex = r'^\d{3}-\d{3}-\d{4}$'
    if re.fullmatch(regex, phone):
        return '(PASS)'  # Change to '' after testing
    else:
        return 'P'


def validate_date(date):
    date_format = "%m/%d/%Y"
    try:
        datetime.strptime(date, date_format)
        return '(PASS)'
    except ValueError:
        return 'D'


def validate_time(time):
    time_format = "%H:%M:%S"
    try:
        datetime.strptime(time, time_format)
        return '(PASS)'
    except ValueError:
        return 'T'


def process_file():
    with open('DataInput.csv', 'r', newline='') as input_file, \
            open('ValidData', 'w', newline='') as valid_file, \
            open('InvalidData.csv', 'w', newline='') as invalid_file:

        reader = csv.reader(input_file, delimiter='|')
        valid_writer = csv.reader(valid_file, delimiter=',')
        invalid_writer = csv.writer(invalid_file, delimiter='|')

        for row in reader:
            error_string = ""
            data_count = len(row)

            if data_count == 6:
                error_string += validate_id(row[0])
                error_string += validate_name(row[1])
                error_string += validate_email(row[2])
                error_string += validate_phone(row[3])
                error_string += validate_date(row[4])
            else:
                error_string = "C"

            print(error_string)


if __name__ == '__main__':
    process_file()
