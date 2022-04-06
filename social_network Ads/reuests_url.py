import json
import requests

url = 'http://127.0.0.1:8009/model'
request_data = json.dumps({'age':40, 'EstimatedSalary':70000})
response = requests.post(url, request_data)
print(response.text)

