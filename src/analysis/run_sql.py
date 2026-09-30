import sqlite3
from pathlib import Path


DATABASE_PATH = Path("data/sales.db")
SQL_FILE = Path("sql/analysis.sql")


with sqlite3.connect(DATABASE_PATH) as connection:
    sql = SQL_FILE.read_text(encoding="utf-8")
    cursor = connection.execute(sql)

    columns = [description[0] for description in cursor.description]
    rows = cursor.fetchall()

    print(columns)

    for row in rows:
        print(row)