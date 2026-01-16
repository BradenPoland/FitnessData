import pandas as pd
from src.database import get_connection

def load_weight() -> pd.DataFrame:
    query = "SELECT * FROM weight"
    with get_connection() as conn:
        return pd.read_sql(query, conn)

def insert_weight(value: float):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO weight (value, created_at) VALUES (?, datetime('now'))",
            (value,)
        )