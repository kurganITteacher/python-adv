from requests import get

# url = 'http://localhost:8000/api/token/'
# user_cred = {'username': 'kpk', 'password': 'pass'}
# response = post(url, data=user_cred)
# resp_data = response.json()
# print(resp_data)

# {'refresh': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0MDE1MDc0OCwiaWF0IjoxNjQwMDY0MzQ4LCJqdGkiOiI4NmRjZGZkNTYyOTE0YjJlOTU1NTJkOWNiNjM0Njc1NyIsInVzZXJfaWQiOjF9.63WwqkZxTCTOuI_qmhs9glsFmcybVO9tuWljmdCPIA0',
#  'access': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQwMDY0NjQ4LCJpYXQiOjE2NDAwNjQzNDgsImp0aSI6IjIyYzZjZjBhOWM1ZTRlYTFhNDFiMWNkNzYwNmQ1MmU0IiwidXNlcl9pZCI6MX0.r7hN-iO19hhTk_ZsQBgtptntR90K3mhnbZrbUP-c7tw'}

url = 'http://localhost:8000/api/users/'
# token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQwMDcxNTc1LCJpYXQiOjE2NDAwNzEyNzUsImp0aSI6IjA4NzZmZWViMDE0MDRhNzc5MTY0Njk4Y2MwMzAwZTczIiwidXNlcl9pZCI6MX0.2Uh77EI0hGkPNROYcetB-mjPziYnqUWbdtixWeisaPk'
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQwMDcxODQ0LCJpYXQiOjE2NDAwNzE1NDQsImp0aSI6IjE3YTBjMTY1NTA5NzRhMzlhMzMwNzc2YmM4MThlMDQ1IiwidXNlcl9pZCI6MX0.p3rGJMZCIvLIbNrmyzvspoDB0jZkUswXBkFTGppbgao'
headers = {'Authorization': f'Bearer {token}'}
print(headers)
response = get(url,
               headers=headers)
resp_data = response.json()
print(resp_data)

