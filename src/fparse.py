import urllib.request


def download_log():
    urllib.request.urlretrieve("https://s3.amazonaws.com/tcmg476/http_access_log", "http_access_log")

