lookup = 'local - - [30/Apr/1995:23:57:25 -0600] "GET index.html HTTP/1.0" 200 2881'

with open("http_access_log") as myFile:
    for num, line in enumerate(myFile, 1):
        if lookup in line:
            print('found at line:', num) 
            print('There are',726736-num, 'entries in the last six months of the log') 
            