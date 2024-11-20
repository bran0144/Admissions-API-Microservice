import requests



url = 'http://127.0.0.1:9003/applications'
data = {'email': "tommy@college.edu"}

headers = {'Content-Type': 'application/json'}

response = requests.get(url, json=data, headers=headers)
print(response.text)