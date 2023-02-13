import re
import os

from regex_parse import http_parse
from log_reader import read_log

log_lines = read_log("http_access_log")

things  = {}

for i in log_lines:
    log_dict = http_parse(i)
    filename = log_dict['day']
    filename2 = log_dict['month']
    filename3 = log_dict['year']
    print(filename, filename2, filename3)
#for x in range(len(log_lines)):
#    print(log_lines[x])