import requests

post_data = {
    "tg_id": 12121,
    "tel_number": "1212121",
    "fio": "Oydinov S",
    "new_square": "122112",
    "section": "1212",
    "floor": "1212",
    "overall_sum": "121221",
    "paid": "2112121",
    "doc_number": "256",
}

# Use 'files' parameter to send files with requests.post
files = {'doc_image': ('photo.jpg', open(r'C:\photo_2024-01-15_05-37-16.jpg', 'rb'), 'image/jpeg')}

response = requests.post('http://127.0.0.1:8000/add/', data=post_data, files=files)

print(response.text)
