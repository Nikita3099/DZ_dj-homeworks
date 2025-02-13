import requests

url = "http://127.0.0.1:8000/api/measurements/"
data = {
    "sensor": 1,
    "temperature": 22.5
}
files = {
    "image": open("photo.jpg", "rb")
}

response = requests.post(url, data=data, files=files)
print(response.json())
