import re
import os

from regex_parse import http_parse
from log_reader import read_log

log_lines = read_log("http_access_log")

things  = {}


counter = 0
for i in log_lines:
    try:
        log_dict = http_parse(i)
        filename = log_dict['response_code']
        if filename[0] == '3':
            counter+=1    
    except:
        pass
print("There are ", counter, " 3xx errors")

