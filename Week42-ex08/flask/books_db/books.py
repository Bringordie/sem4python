import mysql.connector as mysql

test = 'test'


class Book():

    def __init__(self, rating, reviews, book_title, description, number_of_pages, type, price):
        self.rating = rating
        self.reviews = reviews
        self.book_title = book_title
        self.description = description
        self.number_of_pages = number_of_pages
        self.type = type
        self.price = price

    def __str__(self):
        return 'Book {rating}: {reviews}, {book_title}, {description}, {number_of_pages}, {type}, {price}'.format(rating=self.rating, reviews=self.reviews, book_title=self.book_title, description=self.description, number_of_pages=self.number_of_pages, type=self.type, price=self.price)

    def mysql_connect(self):
        db = mysql.connect(
            # connect to the mysql server running in container with service name: db. CAUTION data here are not persisted past container lifespan
            host="db",
            user="root",
            passwd="root",
            db="db",
            # auth_plugin='mysql_native_password'
        )

        return db

    def get_all_books(self):
        # connecting to the database using 'connect()' method
        # db = mysql.connect(
        # connect to the mysql server running in container with service name: db. CAUTION data here are not persisted past container lifespan
        #     host="127.0.0.1",
        #     port="3309",
        #     user="root",
        #     passwd="root",
        #     db="db",
        #     auth_plugin='mysql_native_password'
        # )
        # db.set_charset_collation('utf8')

        # connect to the mysql server running in container with service name: db. CAUTION data here are not persisted past container lifespan
        db = Book.mysql_connect('')

        # Getting all database information of the books
        cur = db.cursor()
        query = 'select * from week42'
        cur.execute(query)

        result = cur.fetchall()
        db.close()

        return result

    def top_10_books(self):
        db = Book.mysql_connect('')
        cur = db.cursor()
        query = 'select * from week42 ORDER BY Rating DESC LIMIT 10'
        cur.execute(query)

        result = cur.fetchall()
        db.close()

        return result

    def add_book(self):
        db = Book.mysql_connect('')
        # engine = create_engine(db)
        # df = pd.DataFrame({'firstname': ['Ulrik', 'Ulla', 'Ulfred'],
        #                    'lastname': ['Volborg', 'Willman', 'Valberg'],
        #                    'startdate': ['2003-03-03', '2001-05-04', '2001-01-04'],
        #                    'enddate': ['2005-08-20', '2005-12-24', '2006-10-30'],
        #                    'salary': ['21000', '32000', '43000']})
        TODO = ''

    def delete_book(self):
        TODO = ''

    def edit_book(self):
        TODO = ''

    def avg_price(self):
        TODO = ''


if __name__ == "__main__":
    # print(Book.get_all_books(''))
    # print(Book.top_10_books(''))
    test = Book("rating123", "reviews", "book_title", "description",
                "number_of_pages", "type", "price")
    print(test)
