from flask import Flask
import database
import os
from sqlalchemy import text
app = Flask(__name__)

@app.route('/')
def query():
    pool = database.connect_unix_socket()
    sql = text("SELECT * FROM test")
    ll = pool.execute(sql)

    return str(ll)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))