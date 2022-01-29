from requests import post

url = 'http://localhost:8000/api-token-auth/'
user_cred = {'username': 'kpk', 'password': 'pass'}
response = post(url, data=user_cred)
resp_data = response.json()
# print(dir(response))
print(resp_data)
