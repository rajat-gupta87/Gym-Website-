import sqlite3

conn = sqlite3.connect("students.db")   # ← यही आपका DB file है
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS progress(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    weight FLOAT NOT NULL,
    entry_date TEXT DEFAULT DATE('now')
);
""")

conn.commit()
conn.close()

print("✔ Progress Table Created Successfully!")
