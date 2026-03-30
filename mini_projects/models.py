"""
create tables if not exists 
and 
runs once when app starts
"""

from .database import get_db_connection

def create_table():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT
        )
    """)
    conn.close()
