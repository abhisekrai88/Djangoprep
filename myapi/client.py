import requests

url = 'http://127.0.0.1:8000/hello/'

headers = {'Authorization': 'Token 057dbb22a838234e8e4289991d6344684facc216'}

r = requests.get(url, headers=headers)