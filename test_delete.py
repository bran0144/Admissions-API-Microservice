import requests
import json


url = 'http://127.0.0.1:9003/delete_application'
data = {'email': "tommy@college.edu",
        'college_name': "Yale University"}

headers = {'Content-Type': 'application/json'}

response = requests.delete(url, data=json.dumps(data), headers=headers)
print(response.text)