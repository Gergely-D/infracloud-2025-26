from flask import Flask, request, render_template, redirect, url_for
import sqlite3
import hashlib
import os

microweb_app = Flask(__name__)

db_name = '/home/app/account_share/accounts.db'

# Zorg dat database bestaat
def init_db():
    db_conn = sqlite3.connect(db_name)
    c = db_conn.cursor()
    # Plain table
    c.execute("""
        CREATE TABLE IF NOT EXISTS USER_PLAIN (
            USERNAME TEXT PRIMARY KEY NOT NULL,
            PASSWORD TEXT NOT NULL
        )
    """)
    # Hashed table
    c.execute("""
        CREATE TABLE IF NOT EXISTS USER_HASH (
            USERNAME TEXT PRIMARY KEY NOT NULL,
            HASH TEXT NOT NULL
        )
    """)
    db_conn.commit()
    db_conn.close()

init_db()

### HOME
@microweb_app.route('/')
def main():
    return render_template("index.html")

### DELETE ALL RECORDS
@microweb_app.route('/delete/all', methods=['POST', 'DELETE'])
def delete_all():
    db_conn = sqlite3.connect(db_name)
    c = db_conn.cursor()
    c.execute("DELETE FROM USER_PLAIN;")
    c.execute("DELETE FROM USER_HASH;")
    db_conn.commit()
    db_conn.close()
    return "All test records deleted"

### SIGNUP V1 (plain text, insecure)
#### CLEAR TEXT PASSWORDS, INSECURE => signup, verify, login
@microweb_app.route('/signup/v1', methods=['GET', 'POST'])
def signup_v1():
    if request.method == 'GET':
        return render_template("login.html", version="v1")

    # POST
    db_conn = sqlite3.connect(db_name)
    c = db_conn.cursor()
    try:
        c.execute(
            "INSERT INTO USER_PLAIN (USERNAME, PASSWORD) VALUES (?, ?)",
            (request.form['username'], request.form['password'])
        )
        db_conn.commit()
    except sqlite3.IntegrityError:
        return "Username has been registered\n"
    finally:
        db_conn.close()

    return "Signup success\n"


    

def verify_plain(username, password):
    db_conn = sqlite3.connect(db_name)
    c = db_conn.cursor()
    sql_query = "SELECT PASSWORD FROM USER_PLAIN WHERE USERNAME = '{0}'".format(username)
    c.execute(sql_query)
    records = c.fetchone()
    db_conn.close()
    if not records:
        return False
    return records[0] == password
### LOGIN V1 (plain text)
@microweb_app.route('/login/v1', methods=['GET', 'POST'])
def login_v1():
    if request.method == 'GET':
        return render_template("login.html", version="v1")

    username = request.form['username']
    password = request.form['password']

    db_conn = sqlite3.connect(db_name)
    c = db_conn.cursor()
    c.execute("SELECT PASSWORD FROM USER_PLAIN WHERE USERNAME = ?", (username,))
    record = c.fetchone()
    db_conn.close()

    if record and record[0] == password:
        return "Login success (plain text)"
    return "Invalid username/password"

### SIGNUP V2 (hashed passwords, secure)
@microweb_app.route('/signup/v2', methods=['GET', 'POST'])
def signup_v2():
    if request.method == 'GET':
        return render_template("signup.html", version="v2")

    username = request.form['username']
    password = request.form['password']
    hashed = hashlib.sha256(password.encode()).hexdigest()

    db_conn = sqlite3.connect(db_name)
    c = db_conn.cursor()
    try:
        c.execute("INSERT INTO USER_HASH (USERNAME, HASH) VALUES (?, ?)", (username, hashed))
        db_conn.commit()
        return "Signup success (hashed)"
    except sqlite3.IntegrityError:
        return "Username already registered"
    finally:
        db_conn.close()

### LOGIN V2 (hashed passwords)
@microweb_app.route('/login/v2', methods=['GET', 'POST'])
def login_v2():
    if request.method == 'GET':
        return render_template("login.html", version="v2")

    username = request.form['username']
    password = request.form['password']
    hashed = hashlib.sha256(password.encode()).hexdigest()

    db_conn = sqlite3.connect(db_name)
    c = db_conn.cursor()
    c.execute("SELECT HASH FROM USER_HASH WHERE USERNAME = ?", (username,))
    record = c.fetchone()
    db_conn.close()

    if record and record[0] == hashed:
        return "Login success (hashed)"
    return "Invalid username/password"

### MAIN
if __name__ == "__main__":
    microweb_app.run(host="0.0.0.0", port=5050)
