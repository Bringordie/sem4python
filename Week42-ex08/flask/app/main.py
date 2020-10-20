from ..books_db import books
from flask import Flask, jsonify, abort, request
# import mysql.connector as mysql
# from ..books_db.books import get_all_books

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World from Flask in a uWSGI Nginx Docker container with \
     Python 3.8 (from the example template)"


@app.route("/api/test")
def asd():
    return books.get_all_books()


# @app.route("/api/books", methods=['GET'])
# def get_all_books():
#     # connecting to the database using 'connect()' method
#     db = mysql.connect(
#         # connect to the mysql server running in container with service name: db. CAUTION data here are not persisted past container lifespan
#         host="db",
#         user="root",
#         passwd="root",
#         db="db"
#     )
#     db.set_charset_collation('utf8')

#     # Getting all database information of the books
#     cur = db.cursor()
#     query = 'select * from week42'
#     cur.execute(query)

#     myresult = cur.fetchall()

#     return jsonify({'books': myresult})


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", debug=True, port=80)
