import psycopg2
from config import host, user, password, db_name

try:
    #connect to exist database 
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

    connection.autocommit = True

    #the cursor for performing database operations
    #cursor = connection.cursor()
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Select version: {cursor.fetchone()}")

    #create a new table 
    with connection.cursor() as cursor:
        if """SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = '[database_name]' AND table_name = 'users';""":
            pass
        else:
            cursor.execute(
                """CREATE TABLE users(
                id serial PRIMARY KEY,
                first_name varchar(50) NOT NULL,
                nick_name varchar(50) NOT NULL);"""
            )
            #connection.commit()
            print("[INFO] Table created succesfully")

    #insert data into table
#    with connection.cursor() as cursor:
#        cursor.execute(
#            """INSERT INTO users (first_name, nick_name) VALUES 
#            ('Oleg', 'barracuda');"""
#        )
#        print("[INFO] Data was succesfully inserted")

    #get data from a table 
#    with connection.cursor() as cursor:
#        cursor.execute(
#            """SELECT nick_name FROM users WHERE first_name = 'Oleg';"""
#        )
#        print(cursor.fetchone())

    #delete whole table 
    with connection.cursor() as cursor:
        cursor.execute(
            """DROP TABLE users"""
        )
        print("[INFO] Table was deleted")

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        #cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")