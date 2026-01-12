from flask import Flask
from flask import request
from flask import render_template
import sqlite3
import hashlib

microweb_app = Flask(__name__)
# voor het mounten van het pad buiten en in de docker te mounten (samenvoegen)
#sudo mkdir -p /home/app/data
#sudo mount --bind \
#>   /home/devasc/labs/tasks/Flask/flask_app_login/account_share \
#>   /home/app/data
#db_name = '/home/devasc/labs/tasks/Flask/flask_app_login/account_share/accounts.db'
db_name = '/home/app/data/accounts.db' # linux mount
#### RE-INTIALIZING DATABASE => deleting all records from test database
@microweb_app.route('/delete/all', methods=['GET', 'DELETE'])
def delete_all():
    db_conn = sqlite3.connect(db_name)
    c = db_conn.cursor()
    sql_statement = "DELETE FROM USER_PLAIN ; "
    c.execute(sql_statement)
    sql_statement = "DELETE FROM USER_HASH ; "
    c.execute(sql_statement)
    db_conn.commit()
    db_conn.close()
    return "Test records deleted\n"

@microweb_app.route('/create/db', methods=['GET'])
def create_db():
    
    db_conn = sqlite3.connect(db_name)
    c = db_conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS USER_PLAIN (USERNAME TEXT PRIMARY KEY NOT NULL,PASSWORD TEXT NOT NULL);")
    c.execute("CREATE TABLE IF NOT EXISTS USER_HASH (USERNAME TEXT PRIMARY KEY NOT NULL,PASSWORD TEXT NOT NULL);")
    db_conn.commit()    
    db_conn.close()
    return "Database created\n"

#### MAIN
if __name__ == "__main__":
    microweb_app.run(host="0.0.0.0", port=5054, threaded=False)#, ssl_context='adhoc')