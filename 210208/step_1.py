import os
import re
import urllib.parse
import urllib.request

import requests

RE_XLS_FILE = re.compile(r'href="([^"]+\.xls)"')


def get_urls(request_url):
    response = requests.get(request_url)
    content = response.content.decode(encoding=response.encoding)
    return RE_XLS_FILE.findall(content)


def url_encode(request_url):
    protocol, address = request_url.split(':', maxsplit=1)
    return ':'.join([protocol, urllib.parse.quote(address)])


def save_files(urls, path):
    if not os.path.isdir(path):
        os.mkdir(path)
    for file_url in urls:
        urllib.request.urlretrieve(
            url_encode(file_url),
            os.path.join(path, file_url.split('/')[-1])
        )


xls_urls = get_urls('https://kpk.kss45.ru/учебная-работа/расписание_пар.html')
save_files(xls_urls, "xls/")
