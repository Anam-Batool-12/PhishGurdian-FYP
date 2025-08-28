import sqlite3
import os

os.makedirs("database", exist_ok=True)

conn = sqlite3.connect("database/quiz.db")
c = conn.cursor()

# Quiz results table
c.execute('''
CREATE TABLE IF NOT EXISTS quiz_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    score INTEGER NOT NULL,
    total INTEGER NOT NULL,
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# URL logs table (fixed with is_phishing)
c.execute('''
CREATE TABLE IF NOT EXISTS url_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL,
    is_phishing INTEGER NOT NULL, -- 1 = phishing, 0 = safe
    result TEXT NOT NULL,
    checked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# Quiz questions table
c.execute('''
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_option TEXT NOT NULL
)
''')

# Insert sample questions (only once)
c.execute("SELECT COUNT(*) FROM questions")
if c.fetchone()[0] == 0:
    sample_questions = [
        ("What is phishing?",
         "A type of fish",
         "A cyber attack to steal info",
         "A social media trend",
         "None of these",
         "B"),
        ("Which one is a strong password?",
         "123456",
         "password",
         "Ab!9$kPz",
         "qwerty",
         "C"),
        ("What should you check before clicking a link?",
         "The color of link",
         "URL and source",
         "How long it is",
         "Who shared it",
         "B")
    ]
    c.executemany('''
        INSERT INTO questions (question, option_a, option_b, option_c, option_d, correct_option)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', sample_questions)

conn.commit()
conn.close()

print("✅ Fresh DB with `is_phishing` fixed created successfully!")
