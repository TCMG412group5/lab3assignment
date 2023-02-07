#Total Number of Entries in the log file
with open(r"src/lab3/http_access_log", 'r') as fp:
    for count, line in enumerate(fp):
        pass
print('Total Lines', count + 1)

file = open('httplogs.txt', 'r')
text = file.read()

#count the requests from the time period log
from dateutil import parser
date = parser.parse("10th of April, 1995")
date
print(matches)
