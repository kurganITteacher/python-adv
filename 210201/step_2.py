import requests

request_url = 'https://kpk.kss45.ru/%D1%83%D1%87%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0/%D1%80%D0%B0%D1%81%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BF%D0%B0%D1%80.html'

response = requests.get(request_url)
content = response.content.decode(encoding=response.encoding)

print(content)

