"""
This module provides a function for reading log files and returning their lines as a list,
with newline characters stripped.

The module contains the following function:
- read_log: reads a log file and returns its lines as a list
"""

import os

def read_log(file_arg):
    """
    Reads a log file and returns its lines as a list, with newline characters stripped.

    Args:
    file_arg (str): The name of the log file to read.

    Returns:
    list: A list of log lines, with newline characters stripped from each line.

    Example:
    >>> log_lines = read_log("http_log.txt")
    >>> print(log_lines)
    """

    directory = os.path.abspath(os.path.dirname(__file__))

    # Searches for the file name starting from the root directory
    while True:
        file_path = os.path.join(directory, file_arg)
        if os.path.exists(file_path):
            break
        parent = os.path.dirname(directory)
        if parent == directory:
            raise FileNotFoundError(f"File {file_arg} not found.")
        directory = parent

    # Opens the file and iterates through it, adding each line to a list called log_lines
    with open(file_path, "r", encoding="utf-8") as file:
        log_lines = []
        # Iterates through the file, strips out \n in each entry, and adds them to a list
        for line in file:
            line = line.rstrip("\n")
            log_lines.append(line)

    return log_lines
