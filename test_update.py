import requests
import json


url = 'http://127.0.0.1:9003/update_application'
data = {'email': "joe@college.edu",
        'college_name': "Yale University",
        'location': "New Haven, CT",
        'date_submitted': '75,000',
        'status': "applied",
        'ranking': '3',
        'decision': "admitted"}

headers = {'Content-Type': 'application/json'}

response = requests.put(url, data=json.dumps(data), headers=headers)
print(response.text)