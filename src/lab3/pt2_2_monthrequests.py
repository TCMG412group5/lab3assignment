import re
import os
from regex_parse import http_parse
from log_reader import read_log
log_lines = read_log("http_access_log")

things  = {}
for i in log_lines:
    log_dict = http_parse(i)
    filename = log_dict['month']+ " "+log_dict['year']
    if filename in things:
        things[filename] += 1
    else:
        things[filename] = 1
    #   print(filename, filename2, filename3)
    
for z in things:
    print("On the month of ", z, "there were ",things[z], " entries")
