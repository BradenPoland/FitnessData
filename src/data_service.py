import pandas as pd
from src.database import get_connection

def load_measurements() -> pd.DataFrame:
    query = "SELECT * FROM test"
    with get_connection() as conn:
        return pd.read_sql(query, conn)

def insert_measurements(value: float):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO test (value, created_at) VALUES (?, datetime('now'))",
            (value,)
        )