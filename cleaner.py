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
        print("Cleaning up database...")
    except Error as e:
        print(e)
    finally:
        return conn

database = create_connection('./jokes.db')

current_target = 1

def find_record_at_current_target(database, key):
    c = database.cursor()
    c.execute("SELECT * FROM master_jokes WHERE id=:key;", {"key": key})
    #print("Current target:\n")
    #print(c.fetchall())
    return c.fetchall()


def find_all_records_not_current_target(database, key):
    c = database.cursor()
    c.execute("SELECT * FROM master_jokes WHERE id!=:key", {"key": key})
    #print("All other rows:\n")
    #print(c.fetchall())
    return c.fetchall()


def return_last_row_id(database):
    c = database.cursor()
    c.execute("SELECT * FROM master_jokes ORDER BY id DESC LIMIT 1;")
    return c.fetchall()[0][0]


def delete_row_by_key(database, key):
    c = database.cursor()
    c.execute("DELETE FROM master_jokes WHERE id=:key", {"key": key})
    database.commit()


def main_database_cleaner(database, key):
    matches_found = 0
    total_rows = return_last_row_id(database)
    while key <= total_rows:
        current_row_for_inspection = find_record_at_current_target(database, key)
        all_other_rows = find_all_records_not_current_target(database, key)

        for entry in all_other_rows:
            if current_row_for_inspection != []:
                if entry[1] == current_row_for_inspection[0][1]:
                    if entry[2] == current_row_for_inspection[0][2]:
                        matches_found += 1
                        delete_row_by_key(database, current_row_for_inspection[0][0])
        
        key += 1
    
    print("%d duplicates deleted" % matches_found)

def find_jokes_that_remain(database):
    return return_last_row_id(database)

main_database_cleaner(database, current_target)

print("Database closed...")
print("%d jokes remain" % find_jokes_that_remain(database))
print("Happy jokin'")
database.close()
