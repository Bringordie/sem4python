# Enable
from books_db import books as book
from flask import Flask, jsonify, abort, request
import sqlalchemy as s_a

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World from Flask in a uWSGI Nginx Docker container with \
     Python 3.8 (from the example template)"


@app.route("/api/add_csv", methods=['GET'])
def add_csv_books():
    return book.Book.insert_data_from_sheet('')


@app.route("/api/books", methods=['GET'])
def get_all_books():
    return jsonify({'books': book.Book.get_all_books('')})


@app.route("/api/books/top10", methods=['GET'])
def get_top10():
    return jsonify({'Top 10 Books': book.Book.top_10_books('')})


@app.route("/api/books/newbook", methods=['POST'])
def create_book():
    if not request.json or not 'book_title' in request.json:
        abort(400)
    print(request.json)
    rating = request.json['rating']
    reviews = request.json['reviews']
    book_title = request.json['book_title']
    description = request.json['description']
    number_of_pages = request.json['number_of_pages']
    booktype = request.json['booktype']
    price = request.json['price']

    newbook = book.Book(rating, reviews, book_title,
                        description, number_of_pages, booktype, price)
    return newbook.add_book(), 201


@app.route("/api/book/deletebook/<int:book_id>", methods=['DELETE'])
def delete_book(book_id):
    return book.Book.delete_book('', book_id)


@app.route("/api/book/editbook/<int:book_id>", methods=['PUT'])
def edit_book(book_id):
    if not request.json or not 'book_title' in request.json:
        abort(400)
    print(request.json)
    rating = request.json['rating']
    reviews = request.json['reviews']
    book_title = request.json['book_title']
    description = request.json['description']
    number_of_pages = request.json['number_of_pages']
    booktype = request.json['booktype']
    price = request.json['price']

    editbook = book.Book(rating, reviews, book_title,
                         description, number_of_pages, booktype, price)
    return editbook.edit_book(book_id), 201


@app.route("/api/book/avgprice", methods=['GET'])
def average_book_price():
    return book.Book.avg_price('')


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", debug=True, port=80)
