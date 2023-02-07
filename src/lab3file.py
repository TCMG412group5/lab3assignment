#please run this file where all of the code is on 


#code to retrieve online file 
import requests


url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
r = requests.get(url, allow_redirects=True)

open('http_access_log', 'wb').write(r.content)

#Total Number of Entries in the log file
with open(r"src/lab3/http_access_log", 'r') as fp:
    for count, line in enumerate(fp):
        pass
print('The total requests represented by the log is:', count + 1)
