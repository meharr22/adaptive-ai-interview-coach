import sqlite3

conn = sqlite3.connect(
    "interviews.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS interview_history(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT,
    average_score REAL,
    verdict TEXT
)
""")

conn.commit()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

conn.commit()
def create_user(
    username,
    password
):

    cursor.execute(
        """
        INSERT INTO users(
            username,
            password
        )
        VALUES (?,?)
        """,
        (username,password)
    )

    conn.commit()
def get_user(username):

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE username=?
        """,
        (username,)
    )

    return cursor.fetchone()