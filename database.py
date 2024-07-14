import sqlite3

DATABASE = './customers.db'

with sqlite3.connect(DATABASE) as db:
    c = db.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS customer_accounts (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            balance INTEGER
        );''')
    c.execute('''
        INSERT OR IGNORE INTO customer_accounts (id, name, balance) 
        VALUES 
            (1, 'Max', 100),
            (2, 'Lewis', 50)
    ''')


def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
        for idx, value in enumerate(row))

def query_db(query, args=(), single_result=False):
    with sqlite3.connect(DATABASE) as db:
        db.row_factory = make_dicts
        cursor = db.execute(query, args)
        results = cursor.fetchall()
        cursor.close()
        return (results[0] if results else None) if single_result else results
