import sqlite3


with sqlite3.connect('movies.db') as conn:
    c = conn.cursor()

    c.execute('DROP TABLE IF EXISTS new_movies')
    c.execute('CREATE TABLE new_movies (title TEXT, year INT, votes txt, \
    release_date text, rating INT, metascore INT)')
"""
with sqlite3.connect('test.db') as conn:
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS cars')
    c.execute('CREATE TABLE cars (MAKE TEXT DEFAULT NULL, MODEL TEXT DEFAULT NULL, COST INT DEFAULT NULL)')

import sqlite3
with sqlite3.connect('somedb.db') as conn:
    c = conn.cursor()
    c.execute('CREATE TABLE cars (MAKE TEXT, MODEL TEXT, COST TEXT)')

"""