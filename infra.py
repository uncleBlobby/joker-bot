import praw
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


def scrape_sub(subname, reddit, database, jokes_added):
    sub = reddit.subreddit(subname)
    print("Scraping /r/%s..." % subname)

    for submission in sub.hot(limit=50):
        joke = (submission.title, submission.selftext, date.today().strftime("%Y-%m-%d"))
        if subname == 'cleanjokes':
            jokeID = add_clean_joke(database, joke)
            
        if subname == 'dadjokes':
            jokeID = add_dad_joke(database, joke)
            
        if subname == 'jokes':
            jokeID = add_joke(database, joke)
            
        if subname == 'darkjokes':
            jokeID = add_dark_joke(database, joke)
            
        jokes_added += 1
    print("/r/%s scraped..." % subname)