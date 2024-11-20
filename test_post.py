import requests

url = 'http://127.0.0.1:9003/applications'

data = {'email': "tommy@college.edu",
        'collegeName': "Yale University",
        'location': "New Haven, CT",
        'date_submitted': '65,000',
        'status': "applied",
        'ranking': '3',
        'decision': "waitlisted"}

headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=data, headers=headers)
print(response.text)