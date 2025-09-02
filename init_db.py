import sqlite3
import os

os.makedirs("database", exist_ok=True)

conn = sqlite3.connect("database/phishguardian.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS url_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL,
    result TEXT NOT NULL,
    checked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()
print("✅ Database initialized successfully")
