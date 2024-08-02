import sqlite3

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS users (
                   username TEXT PRIMARY KEY,
                   password TEXT,
                   face_data BLOB
                   )
                ''')
    conn.commit()
    conn.close()