import sqlite3




#create db
'''
db = sqlite3.connect('data.db')
c = db.cursor()
c.execute("""CREATE TABLE admin(
    user_id text,
    user_name text,
    user_surname text,
    a1 text,
    a2 text,
    a3 text,
    a4 text,
    d1 text,
    d2 text,
    d3 text,
    d4 text,
    comment_a text,
    comment_d text
)""")
db.commit()
db.close()

'''


def add(user_id, user_name, user_surname, a1, a2, a3, a4, d1, d2, d3, d4, comment_a, comment_d):
    db = sqlite3.connect('data.db')
    c = db.cursor()
    c.execute(f" INSERT INTO admin VALUES ('{user_id}', '{user_name}', '{user_surname}', '{a1}', '{a2}', '{a3}', '{a4}', '{d1}', '{d2}', '{d3}', '{d4}', '{comment_a}', '{comment_d}') ")
    db.commit()
    db.close()

def find_by_id(row_id):
    db = sqlite3.connect('data.db')
    c = db.cursor()
    c.execute(f"SELECT * FROM admin WHERE rowid='{row_id}'")
    return c.fetchall()

def append_4(a):
    if (len(a) < 4):
        while len(a) != 4:
            a.append('0')
    return a

def find_all_id():
    db = sqlite3.connect('data.db')
    c = db.cursor()
    c.execute("SELECT user_id FROM admin")
    return c.fetchall()
