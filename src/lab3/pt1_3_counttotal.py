#Total Number of Entries in the log file
with open("http_access_log", 'r') as fp:
    for count, line in enumerate(fp):
        pass
print('Total Lines', count + 1)
