import sqlite3
from pathlib import Path

DB_PATH = Path("data.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS weight (
                id INTEGER PRIMARY KEY,
                value FLOAT,
                created_at TEXT
            )
        """)