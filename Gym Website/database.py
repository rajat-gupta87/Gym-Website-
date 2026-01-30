import sqlite3

# ==========================
# DATABASE CONFIG
# ==========================
DB = "gym.db"

def connect():
    """Create & return DB connection."""
    return sqlite3.connect(DB, check_same_thread=False)

# ==========================
# TABLE CREATION FUNCTION
# ==========================
def init_db():
    conn = connect()
    cur = conn.cursor()

    # ---------------- USERS TABLE ----------------
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        age INTEGER,
        weight REAL,
        height REAL
    );
    """)

    # ---------------- PROGRESS LOG ----------------
    cur.execute("""
    CREATE TABLE IF NOT EXISTS progress(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        weight REAL NOT NULL,
        date TEXT NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(id)
    );
    """)

    # ---------------- AI WORKOUT / DIET PLANS ----------------
    cur.execute("""
    CREATE TABLE IF NOT EXISTS plans(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT,          -- "workout" / "diet"
        level TEXT,         -- fatloss / muscle / beginner etc
        content TEXT        -- plan full text
    );
    """)

    conn.commit()
    conn.close()

    print("📦 Database initialized successfully ✔")

# ==========================
# RUN DIRECTLY = INIT DB
# ==========================
if __name__ == "__main__":
    init_db()
