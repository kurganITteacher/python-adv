import locale
import os
import re
import urllib.parse
import urllib.request
from datetime import datetime
from sys import getsizeof

locale.setlocale(locale.LC_ALL, "ru")

import requests

RE_XLS_FILE = re.compile(r'href="([^"]+\.xls)"')
RE_XLS_DATE = re.compile(r'(?P<start_dt>\d+)-(?P<end_dt>\d+)\s(?P<month>[а-я]+)\b')

print(RE_XLS_DATE)

# RE_SHORT_DATE = re.compile(r'(\d{2})\.(\d{4})')
# MONTHES = {'02': 'фев', '03': 'мар'}
urls_cached = [
    'https://kpk.kss45.ru/attachments/article/2770/Расписание на 8-13 февраля по группам 2.xls',
    'https://kpk.kss45.ru/attachments/article/2770/Расписание на 8-13 февраля по группам 2.xls',
    'https://kpk.kss45.ru/attachments/article/2770/Расписание на 8-13 февраля по преподавателям А-Л 2.xls',
    'https://kpk.kss45.ru/attachments/article/2770/Расписание на 8-13 февраля по преподавателям А-Л 2.xls',
    'https://kpk.kss45.ru/attachments/article/2770/Расписание на 8-13 февраля по преподавателям М-Щ 2.xls',
    'https://kpk.kss45.ru/attachments/article/2770/Расписание на 8-13 февраля по преподавателям М-Щ 2.xls',
    'https://kpk.kss45.ru/attachments/article/2770/Расписание на 8-13 февраля по аудиториям 2.xls',
    'https://kpk.kss45.ru/attachments/article/2770/Расписание на 8-13 февраля по аудиториям 2.xls',
    'https://kpk.kss45.ru/attachments/article/2759/Расписание на 1-6 февраля по группам3.xls',
    'https://kpk.kss45.ru/attachments/article/2759/Расписание на 1-6 февраля по группам3.xls',
    'https://kpk.kss45.ru/attachments/article/2759/Расписание на 1-6 февраля по преподавателям А-Л3.xls',
    'https://kpk.kss45.ru/attachments/article/2759/Расписание на 1-6 февраля по преподавателям А-Л3.xls',
    'https://kpk.kss45.ru/attachments/article/2759/Расписание на 1-6 февраля по преподавателям М-Щ3.xls',
    'https://kpk.kss45.ru/attachments/article/2759/Расписание на 1-6 февраля по преподавателям М-Щ3.xls',
    'https://kpk.kss45.ru/attachments/article/2759/Расписание на 1-6 февраля по аудиториям2.xls',
    'https://kpk.kss45.ru/attachments/article/2759/Расписание на 1-6 февраля по аудиториям2.xls',
    'https://kpk.kss45.ru/attachments/article/2744/Расписание на 25-30 января по группам3.xls',
    'https://kpk.kss45.ru/attachments/article/2744/Расписание на 25-30 января по группам3.xls',
    'https://kpk.kss45.ru/attachments/article/2744/Расписание на 25-30 января по преподавателям А-Л 2.xls',
    'https://kpk.kss45.ru/attachments/article/2744/Расписание на 25-30 января по преподавателям А-Л 2.xls',
    'https://kpk.kss45.ru/attachments/article/2744/Расписание на 25-30 января по преподавателям М-Щ 2.xls',
    'https://kpk.kss45.ru/attachments/article/2744/Расписание на 25-30 января по преподавателям М-Щ 2.xls',
    'https://kpk.kss45.ru/attachments/article/2744/Расписание на 25-30 января по аудиториям2.xls',
    'https://kpk.kss45.ru/attachments/article/2744/Расписание на 25-30 января по аудиториям2.xls',
    'https://kpk.kss45.ru/attachments/article/2743/Расписание на 18-23 января по преподавателям М-Щ2.xls',
    'https://kpk.kss45.ru/attachments/article/2743/Расписание на 18-23 января по преподавателям М-Щ2.xls',
    'https://kpk.kss45.ru/attachments/article/2743/Расписание на 18-23 января по преподавателям А-Л2.xls',
    'https://kpk.kss45.ru/attachments/article/2743/Расписание на 18-23 января по преподавателям А-Л2.xls',
    'https://kpk.kss45.ru/attachments/article/2743/Расписание на 18-23 января по группам2.xls',
    'https://kpk.kss45.ru/attachments/article/2743/Расписание на 18-23 января по группам2.xls',
    'https://kpk.kss45.ru/attachments/article/2743/Расписание на 18-23 января по  аудиториям.xls',
    'https://kpk.kss45.ru/attachments/article/2743/Расписание на 18-23 января по  аудиториям.xls',
    'https://kpk.kss45.ru/attachments/article/2737/Расписание на 12-16 января по группам 2.xls',
    'https://kpk.kss45.ru/attachments/article/2737/Расписание на 12-16 января по группам 2.xls',
    'https://kpk.kss45.ru/attachments/article/2737/Расписание на 12-16 января по преподавателям А-Л2.xls',
    'https://kpk.kss45.ru/attachments/article/2737/Расписание на 12-16 января по преподавателям А-Л2.xls',
    'https://kpk.kss45.ru/attachments/article/2737/Расписание на 12-16 января по преподавателям М-Щ 2.xls',
    'https://kpk.kss45.ru/attachments/article/2737/Расписание на 12-16 января по преподавателям М-Щ 2.xls',
    'https://kpk.kss45.ru/attachments/article/2737/Расписание на 12-16 января по аудиториям.xls',
    'https://kpk.kss45.ru/attachments/article/2737/Расписание на 12-16 января по аудиториям.xls',
    'https://kpk.kss45.ru/attachments/article/2714/Расписание на 28-31 декабря по группам.xls',
    'https://kpk.kss45.ru/attachments/article/2714/Расписание на 28-31 декабря по группам.xls',
    'https://kpk.kss45.ru/attachments/article/2714/Расписание на 28-31 декабря по преподавателям А-Л.xls',
    'https://kpk.kss45.ru/attachments/article/2714/Расписание на 28-31 декабря по преподавателям А-Л.xls',
    'https://kpk.kss45.ru/attachments/article/2714/Расписание на 28-31 декабря по преподавателям М-Щ.xls',
    'https://kpk.kss45.ru/attachments/article/2714/Расписание на 28-31 декабря по преподавателям М-Щ.xls',
    'https://kpk.kss45.ru/attachments/article/2714/Расписание на 28-31 декабря по аудиториям.xls',
    'https://kpk.kss45.ru/attachments/article/2714/Расписание на 28-31 декабря по аудиториям.xls',
    'https://kpk.kss45.ru/attachments/article/2713/Расписание на 21-26 декабря по группам.xls',
    'https://kpk.kss45.ru/attachments/article/2713/Расписание на 21-26 декабря по группам.xls',
    'https://kpk.kss45.ru/attachments/article/2713/Расписание на 21-26 декабря по преподавателям А-Л.xls',
    'https://kpk.kss45.ru/attachments/article/2713/Расписание на 21-26 декабря по преподавателям А-Л.xls',
    'https://kpk.kss45.ru/attachments/article/2713/Расписание на 21-26 декабря по преподавателям М-Щ.xls',
    'https://kpk.kss45.ru/attachments/article/2713/Расписание на 21-26 декабря по преподавателям М-Щ.xls',
    'https://kpk.kss45.ru/attachments/article/2713/Расписание на 21-26 декабря по аудиториям.xls',
    'https://kpk.kss45.ru/attachments/article/2713/Расписание на 21-26 декабря по аудиториям.xls',
    'https://kpk.kss45.ru/attachments/article/2703/Расписание на 14-19 декабря по группам2.xls',
    'https://kpk.kss45.ru/attachments/article/2703/Расписание на 14-19 декабря по группам2.xls',
    'https://kpk.kss45.ru/attachments/article/2703/Расписание на 14-19 декабря по преподавателям А-Л 2.xls',
    'https://kpk.kss45.ru/attachments/article/2703/Расписание на 14-19 декабря по преподавателям А-Л 2.xls',
    'https://kpk.kss45.ru/attachments/article/2703/Расписание на 14-19 декабря по преподавателям М-Щ2.xls',
    'https://kpk.kss45.ru/attachments/article/2703/Расписание на 14-19 декабря по преподавателям М-Щ2.xls',
    'https://kpk.kss45.ru/attachments/article/2703/Расписание на 14-19 декабря по аудиториям2.xls',
    'https://kpk.kss45.ru/attachments/article/2703/Расписание на 14-19 декабря по аудиториям2.xls',
    'https://kpk.kss45.ru/attachments/article/2688/Расписание на 7-12 декабря по группам 3.xls',
    'https://kpk.kss45.ru/attachments/article/2688/Расписание на 7-12 декабря по группам 3.xls',
    'https://kpk.kss45.ru/attachments/article/2688/Расписание на 7-12 декабря по преподавателям А-Л3.xls',
    'https://kpk.kss45.ru/attachments/article/2688/Расписание на 7-12 декабря по преподавателям А-Л3.xls',
    'https://kpk.kss45.ru/attachments/article/2688/Расписание на 7-12 декабря по преподавателям М-Щ3.xls',
    'https://kpk.kss45.ru/attachments/article/2688/Расписание на 7-12 декабря по преподавателям М-Щ3.xls',
    'https://kpk.kss45.ru/attachments/article/2688/Расписание на 7-12 декабря по аудиториям3.xls',
    'https://kpk.kss45.ru/attachments/article/2688/Расписание на 7-12 декабря по аудиториям3.xls',
    'https://kpk.kss45.ru/attachments/article/2666/Расписание на 30 ноября-5 декабря по аудиториям.xls',
    'https://kpk.kss45.ru/attachments/article/2666/Расписание на 30 ноября-5 декабря по аудиториям.xls',
    'https://kpk.kss45.ru/attachments/article/2666/Расписание на 30 ноября-5 декабря по группам 3.xls',
    'https://kpk.kss45.ru/attachments/article/2666/Расписание на 30 ноября-5 декабря по группам 3.xls',
    'https://kpk.kss45.ru/attachments/article/2666/Расписание на 30 ноября-5 декабря по преподавателям А-Л 3.xls',
    'https://kpk.kss45.ru/attachments/article/2666/Расписание на 30 ноября-5 декабря по преподавателям А-Л 3.xls',
    'https://kpk.kss45.ru/attachments/article/2666/Расписание на 30 ноября-5 декабря по преподавателям М-Щ3.xls',
    'https://kpk.kss45.ru/attachments/article/2666/Расписание на 30 ноября-5 декабря по преподавателям М-Щ3.xls',
    'https://kpk.kss45.ru/attachments/article/2655/Расписание на 23-28 ноября по группам 2.xls',
    'https://kpk.kss45.ru/attachments/article/2655/Расписание на 23-28 ноября по группам 2.xls',
    'https://kpk.kss45.ru/attachments/article/2655/Расписание на 23-28 ноября по преподавателям А-Л2.xls',
    'https://kpk.kss45.ru/attachments/article/2655/Расписание на 23-28 ноября по преподавателям А-Л2.xls',
    'https://kpk.kss45.ru/attachments/article/2655/Расписание на 23-28 ноября по преподавателям М-Щ 2.xls',
    'https://kpk.kss45.ru/attachments/article/2655/Расписание на 23-28 ноября по преподавателям М-Щ 2.xls',
    'https://kpk.kss45.ru/attachments/article/2635/Расписание на 16-21 ноября по группам 3.xls',
    'https://kpk.kss45.ru/attachments/article/2635/Расписание на 16-21 ноября по группам 3.xls',
    'https://kpk.kss45.ru/attachments/article/2635/Расписание на 16-21 ноября по преподавателям А-Л 3.xls',
    'https://kpk.kss45.ru/attachments/article/2635/Расписание на 16-21 ноября по преподавателям А-Л 3.xls',
    'https://kpk.kss45.ru/attachments/article/2635/Расписание на 16-21 ноября по преподавателям М-Щ 3.xls',
    'https://kpk.kss45.ru/attachments/article/2635/Расписание на 16-21 ноября по преподавателям М-Щ 3.xls',
    'https://kpk.kss45.ru/attachments/article/2625/Расписание на 9-14 ноября по группам2.xls',
    'https://kpk.kss45.ru/attachments/article/2625/Расписание на 9-14 ноября по группам2.xls',
    'https://kpk.kss45.ru/attachments/article/2625/Расписание на 9-14 ноября по преподавателям А-Л2.xls',
    'https://kpk.kss45.ru/attachments/article/2625/Расписание на 9-14 ноября по преподавателям А-Л2.xls',
    'https://kpk.kss45.ru/attachments/article/2625/Расписание на 9-14 ноября по преподавателям М-Щ 2.xls',
    'https://kpk.kss45.ru/attachments/article/2625/Расписание на 9-14 ноября по преподавателям М-Щ 2.xls'
]


def _url_encode(request_url):
    protocol, address = request_url.split(':', maxsplit=1)
    return ':'.join([protocol, urllib.parse.quote(address)])


def _get_month_from_path(path):
    month = RE_XLS_DATE.search(path)
    return month and month.group('month')


def get_urls(request_url):
    response = requests.get(request_url)
    content = response.content.decode(encoding=response.encoding)
    return RE_XLS_FILE.findall(content)


def save_files(urls, path):
    if not os.path.isdir(path):
        os.mkdir(path)
    for file_url in urls:
        urllib.request.urlretrieve(
            _url_encode(file_url),
            os.path.join(path, file_url.split('/')[-1])
        )


def filter_by_date(xls_urls, valid_months=['фев', 'мар', 'апр']):
    for url in xls_urls:
        month = _get_month_from_path(url)
        if month is None:
            continue
        month = month.lower()
        for _month in valid_months:
            if _month in month:
                yield url  # return


def parse_dt(dt):
    dt_parsed = datetime.strptime(dt, '%m.%Y')
    return dt_parsed.strftime('%b'), dt_parsed.year


def get_timetable(start_dt=None, end_dt=None):
    # xls_urls = get_urls('https://kpk.kss45.ru/учебная-работа/расписание_пар.html')
    xls_urls = urls_cached
    if start_dt is None and end_dt is None:
        save_files(xls_urls, "xls/")
    xls_urls = filter_by_date(xls_urls)
    print(type(xls_urls), getsizeof(xls_urls))
    # print(*xls_urls)
    path = f"xls/{start_dt}-{end_dt}/"
    if not os.path.isdir(path):
        os.makedirs(path)

    start_dt_rus = parse_dt(start_dt)
    end_dt_rus = parse_dt(end_dt)
    print(start_dt_rus, end_dt_rus)

    save_files(xls_urls, path)
    # Расписание на 8-13 февраля по группам 2
    # Расписание на 12-16 января по аудиториям


# get_timetable('02.2020', '04.2020')  ->  folder '02.2020-04.2020'
# get_timetable()  ->  all files

# get_timetable()
get_timetable('02.2020', '04.2020')
