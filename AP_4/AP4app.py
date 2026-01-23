from flask import Flask, request, render_template
import requests

# AP4: Webform (GET) -> POST -> Python requests call to an API (with auth header)

app = Flask(__name__)

API_KEY = "cisco|oPDek0hz2ppG3r0AH7ctns7ML4HtjFRir3Sq__gPix0"
BASE_URL = "http://library.demo.local/api/v1/books"



HEADERS = {
    "accept": "application/json",
    "X-API-KEY": API_KEY,
    "Content-Type": "application/json",
}

@app.route("/api/v1/books/<int:book_id>", methods=["PUT"])
def api_update_book(book_id):
    if request.headers.get("X-API-KEY") != API_KEY:
        return {"error": "Invalid API key"}, 401

    data = request.get_json(silent=True) or {}
    if data.get("id") != book_id:
        return {"error": "Invalid payload"}, 400

    return {"ok": True, "book": data}, 200

@app.route("/form", methods=["GET"])
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    # 1) Lees form-data
    book_id_str = request.form.get("id", "").strip()
    title = request.form.get("title", "").strip()
    author = request.form.get("author", "").strip()

    # 2) Valideer
    if not book_id_str.isdigit() or not title or not author:
        return "Invalid input. ID must be numeric and title/author required.", 400

    # 3) Definieer book_id (BELANGRIJK)
    book_id = int(book_id_str)

    # 4) Bouw URL CORRECT (geen dubbele slash)
    url = f"{BASE_URL.rstrip('/')}/{book_id}"

    # 5) Payload
    data = {
        "id": book_id,
        "title": title,
        "author": author
    }

    # 6) API call
    resp = requests.put(url, json=data, headers=HEADERS, timeout=10)

    # 7) Toon resultaat
    return (
        f"AP4 OK\n"
        f"PUT {url}\n"
        f"Status: {resp.status_code}\n\n"
        f"Response:\n{resp.text}\n"
    ), resp.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
