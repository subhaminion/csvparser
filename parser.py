import os
import csv
from validators.url import url

filename = "hotels.csv"


def is_valid_name(name):
    if isinstance(name[0], str):
        return True
    return False


def is_valid_url(uri):
    if url(uri[5]):
        return True
    return False


def is_valid_stars(star):
    if 0 <= int(star[2]) <= 5:
        return True
    return False


def validate_fields(line):
    if is_valid_name(line) and is_valid_url(line) and is_valid_stars(line):
        return True
    return False


with open(filename, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    next(csv_reader)
    for line in csv_reader:
    #     if line and validate_fields(line):
        print(line.get('name'))
        break
