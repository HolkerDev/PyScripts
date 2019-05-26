import requests
import json
import base64
from io import BytesIO
from PIL import Image

# open file
im = open('4.jpg', 'rb')
image_read = im.read()

# encode image
image_64_encode = base64.encodebytes(image_read)

print(image_64_encode)
print(str(image_64_encode))

# setup for sending
url = "http://127.0.0.1:5000/api/recognize_with_opencv"
content_type = 'image/jpeg'
headers = {'content-type': content_type}

print(len(image_64_encode))

# response = requests.get('http://127.0.0.1:5000/api/recognize_with_opencv', params={'image': image_64_encode})
response = requests.get(url, params={'image': image_64_encode})
# response = requests.get('http://18.188.155.84:5000/api/recognize_with_opencv', params={'image': image_64_encode})
# response = requests.get('http://127.0.0.1:5000/test', params={'image': image_64_encode})
print(json.loads(response.text))
