"""
This is used for parsing through line in an Apache http log
"""

import re

def http_parse(log_line):
    """Parses an Apache HTTP log line into a dictionary representation.

    Args:
        log_line (str): An Apache HTTP log line in string format.

    Returns:
        dict: Parsed data with the following keys:
            - 'remote_host': IP address of the client.
            - 'day': Day of the month.
            - 'month': Month of the request.
            - 'year': Year of the request.
            - 'hour': Hour of the request.
            - 'minute': Minute of the request.
            - 'second': Second of the request.
            - 'timezone': Timezone of the request.
            - 'method': HTTP method used in the request.
            - 'file': Requested file.
            - 'response_code': HTTP status code returned by the server.
            - 'length': Number of bytes sent in the response.

    Example:
        >>> log = 'local - - [24/Oct/1994:13:41:41 -0600] "GET index.html HTTP/1.0" 200 150'
        >>> print(http_parse(log))
        {
            'remote_host': 'local',
            'day': 24,
            'month': 'Oct',
            'year': 1994,
            'hour': 13,
            'minute': 41,
            'second': 41,
            'timezone': '-0600',
            'method': 'GET',
            'file': 'index.html',
            'response_code': 200,
            'length': 150
        }
    """
    keys = ['remote_host', 'day', 'month', 'year', 'hour',
            'minute', 'second', 'timezone', 'method', 'file',
            'response_code', 'length']
    log_dict = {}

    line_regex = r'(\b(?!-)\w+[\w./?]+\b|[+-]\d+)'

    # Regular expression used to parse the date specifically
    date_regex = r'[\w\d]+'

    # Edge case for if "Villain" or "dasfh" appears instead of "-"
    if re.search(re.escape("Villain"), log_line, re.IGNORECASE):
        log_line_modified = re.sub("Villain", "-", log_line, flags=re.IGNORECASE)
    elif re.search(re.escape("dasfh"), log_line, re.IGNORECASE):
        log_line_modified = re.sub("dasfh", "-", log_line, flags=re.IGNORECASE)
    else:
        log_line_modified = log_line

    # Uses the line_regex regular expression to parse through the log line
    data = re.findall(line_regex, log_line_modified)

    # This is a super hacky way of getting around issues where there is more information after the
    # "GET [file]" portion of the log line

    # Checks if the length of the data array (data after parse) is more than 10
    # This is to cut out any weird corrupted lines that only show
    data_index = [0, 1, 2, 3, 4, 5, 6, 7, -2, -1]
    data_modified = []
    for entry in data_index:
        data_modified.append(data[entry])
    
    # Edge case check for if the length of the packet is equal to "-"
    # If the lenght is equal to "-", set it to 0 instead
    if "HTTP" in data_modified[-2]:
        data_modified[-2] = data_modified[-1]
        data_modified[-1] = str(0)

    data = data_modified

    # This is a super hacky way of getting around issues where there is more information after the
    # "GET [file]" portion of the log line

    # Checks if the length of the data array (data after parse) is more than 10
    # This is to cut out any weird corrupted lines that only show
    data_index = [0, 1, 2, 3, 4, 5, 6, 7, -2, -1]
    data_modified = []
    for entry in data_index:
        data_modified.append(data[entry])
    
    # Edge case check for if the length of the packet is equal to "-"
    # If the lenght is equal to "-", set it to 0 instead
    if "HTTP" in data_modified[-2]:
        data_modified[-2] = data_modified[-1]
        data_modified[-1] = str(0)

    data = data_modified

    keys_count = 0
    # For loop used to create a dictionary that assigns key:value pairs
    for value in data:
        # Since the date is in the first position and I want to parse it further, there is an
        # if-statement to pick up the date to be parsed
        if keys_count == 1:
            date_count = 1
            data_date = re.findall(date_regex, data[1])
            for date_value in data_date:
                log_dict[keys[date_count]] = date_value
                date_count += 1
            # Sets i to 4 to avoid getting picked up by the if statement again and to move to the
            # 4th key in the keys list
            keys_count = 4

        # Else the keys_count iteration is not 1 (aka not a date)
        else:
            log_dict[keys[keys_count]] = value
            keys_count += 1

    return log_dict
