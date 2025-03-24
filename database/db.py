import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "bot.db")
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create tables if not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS warnings (
    user_id INTEGER,
    guild_id INTEGER,
    count INTEGER DEFAULT 0
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS invites (
    user_id INTEGER,
    guild_id INTEGER,
    count INTEGER DEFAULT 0
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS usage (
    user_id INTEGER,
    date TEXT,
    count INTEGER DEFAULT 0
)
""")
# Add more tables as needed for economy, backup, etc.

conn.commit()

def get_db():
    return conn, cursor
