import requests

def log_download():
    url = 'https://s3.amazonaws.com/tcmg476/http_access_log' #url we are downloading from
    r = requests.get(url, allow_redirects=True)
    print(r.headers.get('content-type'))

    open('log', 'wb').write(r.content)