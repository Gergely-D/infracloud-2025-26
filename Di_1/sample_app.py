from flask import Flask, request, render_template

sample = Flask(__name__)

@sample.route("/")
def main():
    # Render HTML from templates/index.html (dynamic via request.remote_addr)
    return render_template("index.html")

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=8080)
