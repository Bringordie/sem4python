import mysql.connector as mysql
# sqlalchemy helped convert strings to dates seamlessly
from sqlalchemy import create_engine
import pandas as pd
import csv
import sys
import os


class Book():

    def __init__(self, rating, reviews, book_title, description, number_of_pages, booktype, price):
        self.rating = rating
        self.reviews = reviews
        self.book_title = book_title
        self.description = description
        self.number_of_pages = number_of_pages
        self.booktype = booktype
        self.price = price

    def __str__(self):
        return 'Book {rating}: {reviews}, {book_title}, {description}, {number_of_pages}, {type}, {price}'.format(rating=self.rating, reviews=self.reviews, book_title=self.book_title, description=self.description, number_of_pages=self.number_of_pages, booktype=self.booktype, price=self.price)

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
        # Creating tables
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

        # Adding data
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
        try:
            cnx = Book.mysql_connect('')
            cursor = cnx.cursor(prepared=True)
            sql = "INSERT INTO week42 (Rating, Reviews, Book_title, Description, Number_Of_Pages, Type, Price) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            book_data = (self.rating, self.reviews, self.book_title,
                         self.description, self.number_of_pages, self.booktype, self.price)
            cursor.execute(sql, book_data)
            cnx.commit()

            # Closing the connection
            cnx.close()
            print('Successfully add Book')
        except mysql.connector.Error as error:
            print("Failed to delete record from table: {}".format(error))
            return error
        return 'Book added'

    def delete_book(self, bookid):
        try:
            cnx = Book.mysql_connect('')
            cursor = cnx.cursor(prepared=True)
            sql = 'delete from week42 where bookid = %s' % (bookid)
            print(sql)

            cursor.execute(sql)
            cnx.commit()

            # Closing the connection
            cnx.close()
            print('Successfully deleted Book')
        except mysql.connector.Error as error:
            print("Failed to delete record from table: {}".format(error))
            return error
        return 'Book: {} has been deleted'.format(bookid)

    def edit_book(self, bookid):
        try:
            cnx = Book.mysql_connect('')
            cursor = cnx.cursor(prepared=True)

            sql_update_query = "update week42 set Rating = \'%s\', Reviews = \'%s\', Book_title = \'%s\', Description = \'%s\', Number_Of_Pages = \'%s\', Type = \'%s\', Price = \'%s\' where bookid = %d" % (
                self.rating, self.reviews, self.book_title, self.description, self.number_of_pages, self.booktype, self.price, bookid)

            cursor.execute(sql_update_query)
            cnx.commit()

            # Closing the connection
            cnx.close()
            print('Successfully edited Book')
        except mysql.connector.Error as error:
            print("Failed to delete record from table: {}".format(error))
            return error
        return 'Book Edited'

    def avg_price(self):
        try:
            cnx = Book.mysql_connect('')
            cursor = cnx.cursor(prepared=True)
            sql = "SELECT AVG(Price) FROM week42"

            cursor.execute(sql)
            result = cursor.fetchone()

            formatted_float = "{:.2f}".format(result[0])
            print('The average of all Books are:', formatted_float)

            # Closing the connection
            cnx.close()
        except mysql.connector.Error as error:
            print("Failed to delete record from table: {}".format(error))
            return error
        return ('The average of all Books are: {}'.format(formatted_float))
