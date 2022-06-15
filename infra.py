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

create_master_jokes_table = """ CREATE TABLE IF NOT EXISTS master_jokes (
                                    id integer PRIMARY KEY,
                                    title text NOT NULL,
                                    joke text,
                                    category text NOT NULL,
                                    createdAt text NOT NULL
                                ); """



def add_joke(conn, joke):

    createdAt = date.today().strftime("%Y-%m-%d")
    sql = ''' INSERT INTO master_jokes(title, joke, category, createdAt)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, joke)
    conn.commit()
    return cur.lastrowid

def add_clean_joke(conn, joke):

    sql = ''' INSERT INTO master_jokes(title, joke, category, createdAt)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, joke)
    conn.commit()
    return cur.lastrowid

def add_dad_joke(conn, joke):
    
    sql = ''' INSERT INTO master_jokes(title, joke, category, createdAt)
            VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, joke)
    conn.commit()
    return cur.lastrowid

def add_dark_joke(conn, joke):
    
    sql = ''' INSERT INTO master_jokes(title, joke, category, createdAt)
            VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, joke)
    conn.commit()
    return cur.lastrowid


def scrape_sub(subname, reddit, database, jokes_added):
    sub = reddit.subreddit(subname)
    print("Scraping /r/%s..." % subname)
    new_jokes = 0
    for submission in sub.hot(limit=50):
        
        if subname == 'cleanjokes':
            joke = (submission.title, submission.selftext, 'clean joke', date.today().strftime("%Y-%m-%d"))
            jokeID = add_clean_joke(database, joke)
            new_jokes += 1
            
        if subname == 'dadjokes':
            joke = (submission.title, submission.selftext, 'dad joke', date.today().strftime("%Y-%m-%d"))
            jokeID = add_dad_joke(database, joke)
            new_jokes += 1
            
        if subname == 'jokes':
            joke = (submission.title, submission.selftext, 'joke', date.today().strftime("%Y-%m-%d"))
            jokeID = add_joke(database, joke)
            new_jokes += 1
            
        if subname == 'darkjokes':
            joke = (submission.title, submission.selftext, 'dark', date.today().strftime("%Y-%m-%d"))
            jokeID = add_dark_joke(database, joke)
            new_jokes += 1
    
    for submission in sub.new(limit=50):

        if subname == 'cleanjokes':
            joke = (submission.title, submission.selftext, 'clean joke', date.today().strftime("%Y-%m-%d"))
            jokeID = add_clean_joke(database, joke)
            new_jokes += 1
            
        if subname == 'dadjokes':
            joke = (submission.title, submission.selftext, 'dad joke', date.today().strftime("%Y-%m-%d"))
            jokeID = add_dad_joke(database, joke)
            new_jokes += 1
            
        if subname == 'jokes':
            joke = (submission.title, submission.selftext, 'joke', date.today().strftime("%Y-%m-%d"))
            jokeID = add_joke(database, joke)
            new_jokes += 1
            
        if subname == 'darkjokes':
            joke = (submission.title, submission.selftext, 'dark', date.today().strftime("%Y-%m-%d"))
            jokeID = add_dark_joke(database, joke)
            new_jokes += 1
            
    print("/r/%s scraped..." % subname)            
    return new_jokes
