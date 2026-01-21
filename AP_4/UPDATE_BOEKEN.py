import requests

API_KEY = "cisco|oPDek0hz2ppG3r0AH7ctns7ML4HtjFRir3Sq__gPix0"
ID = 1001
TITLE = "Return of the king"
AUTHOR = "JR Tolkien"
URL = f"http://library.demo.local/api/v1/books/{ID}"

headers = {
    "accept": "application/json",
    "X-API-KEY": API_KEY,
    "Content-Type": "application/json"
}

data = {
    "id": ID,
    "title": TITLE,
    "author": AUTHOR
}

response = requests.put(URL, json=data, headers=headers)
# print(type(response))
print(response.status_code)