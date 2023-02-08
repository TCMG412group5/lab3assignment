"""
This is used for parsing through line in an Apache http log
"""
import re

LINE = 'local - - [24/Oct/1994:13:41:41 -0600] "GET index.html HTTP/1.0" 200 150'
keys = ['remote_host', 'day', 'month', 'year', 'hour',
        'minute', 'second', 'timezone', 'method', 'file',
        'http_version', 'response_code', 'length']
log_dict = {}

# Regular expression used to parse a single line of the HTTP log
LINE_REGEX = r'(\b(?!-)\w+[\w./]+\b|[+-]\d+)'

# Regular expression used to parse the date specifically
DATE_REGEX = r'[\w\d]+'

# Uses the LINE_REGEX regular expression to parse through the log line
data = re.findall(LINE_REGEX, LINE)

KEYS_COUNT = 0
# For loop used to create a dictionary that assigns key:value pairs
for value in data:
    # Since the date is in the first position and I want to parse it further, there is an
    # if-statement to pick up the date to be parsed
    if KEYS_COUNT == 1:
        DATE_COUNT = 1
        data_date = re.findall(DATE_REGEX, data[1])
        for date_value in data_date:
            log_dict[keys[DATE_COUNT]] = date_value
            DATE_COUNT += 1
        # Sets i to 4 to avoid getting picked up by the if statement again and to move to the
        # 4th key in the keys list
        KEYS_COUNT = 4

    # Else the KEYS_COUNT iteration is not 1 (aka not a date)
    else:
        log_dict[keys[KEYS_COUNT]] = value
        KEYS_COUNT += 1

# Prints the dictionary in a "json"-like format
print('{')
for key, value in log_dict.items():
    print(f'  "{key}": "{value}",')
print('}')
