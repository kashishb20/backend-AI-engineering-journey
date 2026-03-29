""""
opens database connection and 
converts rows -> dictionary-like

"""


import sqlite3

def get_db_connection():
    conn = sqlite3.connect("tasks.db")
    conn.row_factory = sqlite3.Row
    return conn
