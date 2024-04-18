#!/user.bin.env python3

"""
Opening Docstring

GitHub URL: https://github.com/kasnyd/DataValidation
"""

#  Insert Imports As Needed

import re
import csv

__author__ = 'Rivar Yoder | Kaeden Snyder'
__version__ = '1.0'
__date__ = '4/22/2024'
__status__ = 'Development'


# Validate ID
def validate_id(id):
    regex = "^\\d+$"
    if re.compile(regex).match(id):
        return ""
    else:
        return "I"

# Validate Name


def validate_name(name):
    names = name.split(",")
    if len(names) == 2:
        return ""
    else:
        return "N"


def process_file():
    with open('DataInput.csv', 'r') as file, open('InvalidData.csv') as invalid, open('ValidData.csv') as valid:
        reader = csv.reader(file, delimiter='|')
        for row in reader:
            error_string = ""
            data_count = len(row)

            if data_count == 6:
                error_string += validate_id(row[0])
                error_string += validate_name(row[1])
            else:
                error_string = "C"

            print(error_string)


if __name__ == '__main__':
    process_file()
