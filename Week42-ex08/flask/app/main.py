# from ..app import books
# from books_db import books as book
# import books_db.books as book

# Enable
from books_db import books as book
from flask import Flask, jsonify, abort, request
import mysql.connector as mysql
import sqlalchemy as s_a
# import mysql.connector as mysql
# from ..books_db.books import get_all_books

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World from Flask in a uWSGI Nginx Docker container with \
     Python 3.8 (from the example template)"


@app.route("/api/add_csv", methods=['GET'])
def add_csv_books():
    #db = book.Book.mysql_connect('')
    return book.Book.insert_data_from_sheet('')
    # return 'Books has been added from the csv file books'


@app.route("/api/books", methods=['GET'])
def get_all_books():
    return jsonify({'books': book.Book.get_all_books('')})
    # return jsonify({'books': "Book.get_all_books()"})


# @app.route("/test", methods=['GET'])
# def get_all_books123():
#     SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:root@db/db"
#     engine = s_a.create_engine(SQLALCHEMY_DATABASE_URL)
#     connection = engine.connect()
#     query = 'select * from week42'
#     ResultProxy = connection.execute(query)
#     ResultSet = ResultProxy.fetchall()
#     return jsonify({'books': ResultSet})


@app.route("/api/test", methods=['GET'])
def get_all_books2():
    # connecting to the database using 'connect()' method
    db = mysql.connect(
        # connect to the mysql server running in container with service name: db. CAUTION data here are not persisted past container lifespan
        host="db",
        user="root",
        passwd="root",
        db="db",
        # auth_plugin='mysql_native_password'
    )

    # Getting all database information of the books
    cur = db.cursor()
    query = 'select * from week42'
    cur.execute(query)

    myresult = cur.fetchall()

    return jsonify({'books': myresult})


@app.route("/api/test2", methods=['GET'])
def get_all_books3():
    db = book.Book.mysql_connect('')
    db.set_charset_collation('utf8')

    # Getting all database information of the books
    cur = db.cursor()
    query = 'select * from week42'
    cur.execute(query)

    myresult = cur.fetchall()

    return jsonify({'books': myresult})


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", debug=True, port=80)
