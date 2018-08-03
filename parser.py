import io
import csv
import json
from validators.url import url

filename = "hotels.csv"


def is_valid_name(name):
    if isinstance(name.get('name'), str):
        return True
    return False


def is_valid_url(uri):
    if url(uri.get('uri')):
        return True
    return False


def is_valid_stars(star):
    if 0 <= int(star.get('stars')) <= 5:
        return True
    return False


def validate_fields(line):
    if is_valid_name(line) and is_valid_url(line) and is_valid_stars(line):
        return True
    return False


def convert_row(row):
    return f"""<hotel>
        <name>{row.get('name')}</name>
        <address>{row.get('address')}</address>
        <stars>{row.get('stars')}</stars>
        <phone>{row.get('phone')}</phone>
        <uri>{row.get('uri')}</uri>
    </hotel>\n"""


with open(filename) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    rows = list()

    next(csv_reader)
    for line in csv_reader:
        if line and validate_fields(line):
            rows.append(line)

with io.open('test.json', 'w', encoding='utf8') as f:
    json.dump(rows, f, ensure_ascii=False)

with io.open('test.xml', 'w') as f:
    f.write('<hotelListings>')
    for line in rows:
        f.write(convert_row(line))
    f.write('</hotelListings>')
