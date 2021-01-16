import requests

url = 'http://127.0.0.1:8000/hello/'

headers = {'Authorization': 'Token e5b372c472d4e9cb1054e71e36a97137731b3e20'}

r = requests.get(url, headers=headers)
print(r)