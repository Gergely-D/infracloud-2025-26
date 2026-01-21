import requests
import json

APIHOST = "http://library.demo.local"
LOGIN = "cisco"
PASSWORD = "Cisco123!"

def getAuthToken():
    authCreds = (LOGIN, PASSWORD)
    r = requests.post(
        f"{APIHOST}/api/v1/loginViaBasic",
        auth=authCreds
    )
    if r.status_code == 200:
        return r.json()["token"]
    else:
        raise Exception(
            f"Status code {r.status_code} and text {r.text}, while trying to Auth."
        )

def addBook(book, apiKey):
    r = requests.post(
        f"{APIHOST}/api/v1/books",
        headers={
            "Content-type": "application/json",
            "X-API-Key": apiKey
        },
        data=json.dumps(book)
    )
    if r.status_code == 200:
        print(f"Book added successfully: {book['title']}")
    else:
        raise Exception(
            f"Error code {r.status_code} and text {r.text}, while trying to add book."
        )

# API-key ophalen (of hardcoded gebruiken)
apiKey = getAuthToken()
#apiKey = "cisco|ovUo0NepD_YNTbIo4hnHyZwBHpZHC6vOx5PYsLdRIQQ"

# Specifiek boek: The Shining
book = {
    "id": 1001,
    "title": "The Shining",
    "author": "Stephen King",
    "isbn": "9780307743657"
}

# Boek toevoegen via de API
addBook(book, apiKey)