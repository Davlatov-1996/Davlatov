import sqlite3

conn = sqlite3.connect("game.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    name TEXT,
    score INTEGER DEFAULT 0
)
""")
conn.commit()

def save_user(user_id, name):
    cursor.execute("INSERT OR IGNORE INTO users (user_id, name) VALUES (?, ?)", (user_id, name))
    conn.commit()

def update_score(user_id, score):
    cursor.execute("UPDATE users SET score = score + ? WHERE user_id = ?", (score, user_id))
    conn.commit()

def update_name(user_id, name):
    cursor.execute("UPDATE users SET name = ? WHERE user_id = ?", (name, user_id))
    conn.commit()

def get_top():
    cursor.execute("SELECT name, score FROM users ORDER BY score DESC LIMIT 5")
    return cursor.fetchall()