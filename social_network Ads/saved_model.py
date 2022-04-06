import json 
import requests

url  = 'http://127.0.0.1:8009/model'
request_data = json.dumps('model','SVM')
response = request.post(url, request_data)
print(response_text)
