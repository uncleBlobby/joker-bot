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
    #print("Current target:\n")
    #print(c.fetchall())
    return c.fetchall()


def find_all_records_not_current_target(database, key):
    c = database.cursor()
    find_all_nontarget_rows = "SELECT * FROM clean_jokes WHERE id!=:key", {"key": key}
    c.execute("SELECT * FROM clean_jokes WHERE id!=:key", {"key": key})
    #print("All other rows:\n")
    #print(c.fetchall())
    return c.fetchall()


def return_last_row_id(database):
    c = database.cursor()
    c.execute("SELECT * FROM clean_jokes ORDER BY id DESC LIMIT 1;")
    return c.fetchall()[0][0]


def delete_row(database, key):
    c = database.cursor()
    c.execute("DELETE FROM clean_jokes WHERE id=:key", {"key": key})
    database.commit()


def main_database_cleaner(database, key):
    matches_found = 0
    total_rows = return_last_row_id(database)
    while key <= total_rows:
        current_row_for_inspection = find_record_at_current_target(database, key)
        all_other_rows = find_all_records_not_current_target(database, key)

        for entry in all_other_rows:
            #print(entry)
            #print(current_row_for_inspection)
            if current_row_for_inspection != []:
                if entry[1] == current_row_for_inspection[0][1]:
                    if entry[2] == current_row_for_inspection[0][2]:
                        #print("match found!")
                        #print("entry #%d" % entry[0])
                        #print(entry[2])
                        #print("==========================")
                        #print("entry #%d" % current_row_for_inspection[0][0])
                        #print(current_row_for_inspection[0][2])
                        matches_found += 1
                        delete_row(database, entry[0])
        
        key += 1
    
    print("%d matches found" % matches_found)


main_database_cleaner(database, current_target)