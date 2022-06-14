from datetime import date

create_clean_jokes_table = """ CREATE TABLE IF NOT EXISTS clean_jokes (
                                    id integer PRIMARY KEY,
                                    title text NOT NULL,
                                    joke text,
                                    createdAt text NOT NULL
                                ); """

create_dad_jokes_table = """ CREATE TABLE IF NOT EXISTS dad_jokes (
                                    id integer PRIMARY KEY,
                                    title text NOT NULL,
                                    joke text,
                                    createdAt text NOT NULL
                                ); """

create_dark_jokes_table = """ CREATE TABLE IF NOT EXISTS dark_jokes (
                                    id integer PRIMARY KEY,
                                    title text NOT NULL,
                                    joke text,
                                    createdAt text NOT NULL
                                ); """

create_jokes_table = """ CREATE TABLE IF NOT EXISTS jokes (
                                    id integer PRIMARY KEY,
                                    title text NOT NULL,
                                    joke text,
                                    createdAt text NOT NULL
                                ); """



def add_joke(conn, joke):

    createdAt = date.today().strftime("%Y-%m-%d")
    sql = ''' INSERT INTO jokes(title, joke, createdAt)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, joke)
    conn.commit()
    return cur.lastrowid

def add_clean_joke(conn, joke):

    sql = ''' INSERT INTO clean_jokes(title, joke, createdAt)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, joke)
    conn.commit()
    return cur.lastrowid

def add_dad_joke(conn, joke):
    
    sql = ''' INSERT INTO dad_jokes(title, joke, createdAt)
            VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, joke)
    conn.commit()
    return cur.lastrowid

def add_dark_joke(conn, joke):
    
    sql = ''' INSERT INTO dark_jokes(title, joke, createdAt)
            VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, joke)
    conn.commit()
    return cur.lastrowid