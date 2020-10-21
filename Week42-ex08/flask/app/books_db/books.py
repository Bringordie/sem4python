import mysql.connector as mysql
# sqlalchemy helped convert strings to dates seamlessly
from sqlalchemy import create_engine
import pandas as pd
import csv
import sys
import os


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

    def insert_data_from_sheet(self):
        filename = "./books_db/prog_book.csv"
        tablename = "week42"
        try:
            cnx = mysql.connect(host="db", user="root", passwd="root", db="db")
            cursor = cnx.cursor(prepared=True)
            # Dropping EMPLOYEE table if already exists.
            cursor.execute("DROP TABLE IF EXISTS %s" % (tablename))

            # Reading the header
            with open(filename) as f:
                reader = csv.reader(f)
                header_row = next(reader)

            # Creating table as per requirement
            sql = ''
            # print(len(header_row))
            for idx, header in enumerate(header_row):
                if (idx == 0):
                    sql += 'CREATE TABLE %s(bookid INTEGER not null AUTO_INCREMENT unique,' % (
                        tablename)
                if (idx != len(header_row)-1):
                    sql += '%s VARCHAR(2000) not null, ' % (header)
                else:
                    sql += '%s VARCHAR(2000) not null) ' % (header)

            cursor.execute(sql)

            # Closing the connection
            cnx.close()
            print('Successfully created tables')
        except:
            e = sys.exc_info()[0]
            return e

        try:
            # reading csv file
            data = pd.read_csv(filename)

            # Creating a connection
            con_str = "mysql+mysqlconnector://root:root@db/db"
            engine = create_engine(con_str)

            # Re-writing it to map
            df = data.applymap(str)
            # Inserting it to the database
            df.to_sql(tablename, con=engine, if_exists='append', index=False)
            print('Successfully inserted data')
        except:
            print('Something went wrong see error')
        return 'Everything went okay. Data was pushed to the Database'

    def get_all_books(self):
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
    # test = Book("rating123", "reviews", "book_title", "description",
    #             "number_of_pages", "type", "price")
    # print(test)
    print(Book.insert_data_from_sheet(''))
