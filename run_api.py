import requests
import json

data = requests.get('http://127.0.0.1:8000')
data = json.loads(data.text)
print(data)
post_data = {
    "tg_id": 1231456,  
    "tel_number": "123-456-7890",
    "fio": "John Doe",
    "new_square": 50.0,
    "section": 1,
    "floor": 3,
    "overall_sum": 500.0,
    "paid": 200.0
}

# Make the POST request
response = requests.post('http://127.0.0.1:8000/add/', data=post_data)

print(data)