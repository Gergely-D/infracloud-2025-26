from flask import Flask          # de Flask-app zelf
from flask import request        # om POST- en GET-data te lezen
from flask import render_template # om HTML-templates te renderen
import sqlite3                   # SQLite database verbinding
import hashlib
microweb_app = Flask(__name__)
db_name = '/home/app/data/accounts.db'

@microweb_app.route('/signup/v1', methods=['GET', 'POST'])
def signup_v1():
    if request.method == 'GET':
        return render_template("signup_v1.html")

    db = sqlite3.connect(db_name)
    c = db.cursor()
    try:
        c.execute(
            "INSERT INTO USER_PLAIN (USERNAME, PASSWORD) VALUES (?, ?)",
            (request.form['username'], request.form['password'])
        )
        db.commit()
    except sqlite3.IntegrityError:
        return "Username has been registered (v1, insecure)\n"
    finally:
        db.close()

    return "Signup success (v1, insecure)\n"


def verify_plain(username, password):
    db = sqlite3.connect(db_name)
    c = db.cursor()
    c.execute(
        "SELECT PASSWORD FROM USER_PLAIN WHERE USERNAME = ?",
        (username,)
    )
    record = c.fetchone()
    db.close()
    return record and record[0] == password


@microweb_app.route('/signin/v1', methods=['GET', 'POST'])
def signin_v1():
    if request.method == 'GET':
        return render_template("signin_v1.html")

    if verify_plain(request.form['username'], request.form['password']):
        return "Signin success (v1, insecure)\n"
    else:
        return "Invalid username/password\n"
@microweb_app.route('/signup/v2', methods=['GET', 'POST'])
def signup_v2():
    if request.method == 'GET':
        return render_template("signup_v2.html")

    hash_value = hashlib.sha256(
        request.form['password'].encode()
    ).hexdigest()

    db = sqlite3.connect(db_name)
    c = db.cursor()
    try:
        c.execute(
            "INSERT INTO USER_HASH (USERNAME, HASH) VALUES (?, ?)",
            (request.form['username'], hash_value)
        )
        db.commit()
    except sqlite3.IntegrityError:
        return "Username has been registered (v2)\n"
    finally:
        db.close()

    return "Signup success (v2, hash)\n"


def verify_hash(username, password):
    db = sqlite3.connect(db_name)
    c = db.cursor()
    c.execute(
        "SELECT HASH FROM USER_HASH WHERE USERNAME = ?",
        (username,)
    )
    record = c.fetchone()
    db.close()

    if not record:
        return False

    return record[0] == hashlib.sha256(password.encode()).hexdigest()


@microweb_app.route('/signin/v2', methods=['GET', 'POST'])
def signin_v2():
    if request.method == 'GET':
        return render_template("signin_v2.html")

    if verify_hash(request.form['username'], request.form['password']):
        return "Signin success (v2, hash)\n"
    else:
        return "Invalid username/password\n"

if __name__ == "__main__":
    microweb_app.run(host="0.0.0.0", port=5055, debug=False)