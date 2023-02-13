import requests
import os

if (os.path.exists('http_access_log')):
    #os.remove('http_access_log')
    print("File Already Exists!")
else:
    url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    r = requests.get(url, allow_redirects=True)
    open('http_access_log', 'wb').write(r.content)