import mysql.connector as mysql


def get_all_books():
    # connecting to the database using 'connect()' method
    db = mysql.connect(
        # connect to the mysql server running in container with service name: db. CAUTION data here are not persisted past container lifespan
        host="127.0.0.1",
        port="3309",
        user="root",
        passwd="root",
        db="db",
        auth_plugin='mysql_native_password'
    )
    db.set_charset_collation('utf8')

    # Getting all database information of the books
    cur = db.cursor()
    query = 'select * from week42'
    cur.execute(query)

    myresult = cur.fetchall()

    return myresult


if __name__ == "__main__":
    print(get_all_books())
