import psycopg2
from psycopg2 import Error

def connect_to_db(username='raywu1990', password='test', host='127.0.0.1', port='5432', database='dvdrental'):
    try:
        connection = psycopg2.connect(user=username, password=password, host=host, port=port, database=database)
        cursor = connection.cursor()
        return cursor, connection
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return None, None

def disconnect_from_db(connection, cursor):
    if connection:
        cursor.close()
        connection.close()

def run_and_fetch_sql(cursor, sql_string=""):
    try:
        cursor.execute(sql_string)
        return cursor.fetchall()
    except (Exception, Error) as error:
        print("Errors while executing SQL: ", error)
        return -1

