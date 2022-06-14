import sqlite3
from sqlite3 import Error

# query database based on primary key
# query database on all NOT EQUAL to primary key
# if any are an "identical" match, remove second item from db
# increment primary key, repeat

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        return conn

database = create_connection('./jokes.db')



current_target = 1

def find_record_at_current_target(database, key):
    c = database.cursor()
    find_row_sql = "SELECT FROM clean_jokes WHERE id=:key;", {"key": key}
    c.execute("SELECT * FROM clean_jokes WHERE id=:key;", {"key": key})
    print(c.fetchall())

find_record_at_current_target(database, 1)
