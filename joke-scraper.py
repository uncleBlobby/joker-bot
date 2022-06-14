import praw
import sqlite3
from sqlite3 import Error

from datetime import date

from infra import *

jokes_added = 0

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

database = create_connection('./jokes.db')
print("Database connection opened...")


if database is not None:
    create_table(database, create_clean_jokes_table)
    create_table(database, create_dad_jokes_table)
    create_table(database, create_jokes_table)
    create_table(database, create_dark_jokes_table)
else:
    print("Error! cannot create the database connection.")

reddit = praw.Reddit(
    client_id='hRTuCmK-uQjV0er8qbmQLQ',
    client_secret='ij0GiDndP50XwDQkq7RAeWyWIsIXJQ',
    user_agent='test-bot-8910:a test bot by /u/test-bot-8910',
    username='test-bot-8910',
    password='q5AKiz9tLm4jPij'
)
print("Reddit API connection opened...")

jokes_added = scrape_sub('cleanjokes', reddit, database, jokes_added)
print("%d jokes added to database" % jokes_added)
jokes_added = scrape_sub('dadjokes', reddit, database, jokes_added)
print("%d jokes added to database" % jokes_added)
jokes_added = scrape_sub('jokes', reddit, database, jokes_added)
print("%d jokes added to database" % jokes_added)
jokes_added = scrape_sub('darkjokes', reddit, database, jokes_added)
print("%d jokes added to database" % jokes_added)

database.close()

print("Database closed...")
print("Happy jokin'\n")