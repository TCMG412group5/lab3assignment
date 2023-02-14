import re
import os

import numpy as np #Dont think I used this
from regex_parse import http_parse
from log_reader import read_log
#Makes a list of the log lines
log_lines = read_log("http_access_log")
#Creates the counter list that holds how many logs were processed on each day.
things  = {}
#Iterates through the log lines looking at each date. If the date is not in the things list, it gets added. If the date is already in the things list, the value for that date is incremented by 1.
#This Creates another list with each date, as well as how many logs that were processed on that day.
for i in log_lines:
    try:
        log_dict = http_parse(i)
        filename = log_dict['day']+log_dict['month']+log_dict['year']
        if filename in things:
            things[filename] += 1
        else:
            things[filename] = 1
     #   print(filename, filename2, filename3)
    except:
        pass
    
for z in things:
    print("On ", z, "there were ",things[z], " entries")


