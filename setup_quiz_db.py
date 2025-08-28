# import sqlite3

# # Connect to the database (creates file if not exists)
# conn = sqlite3.connect("database/quiz.db")
# cur = conn.cursor()

# # Create table for quiz questions
# cur.execute("""
# CREATE TABLE IF NOT EXISTS questions (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     question TEXT NOT NULL,
#     option1 TEXT NOT NULL,
#     option2 TEXT NOT NULL,
#     option3 TEXT NOT NULL,
#     option4 TEXT NOT NULL,
#     correct_answer TEXT NOT NULL
# )
# """)

# # Insert sample questions
# cur.execute("INSERT INTO questions (question, option1, option2, option3, option4, correct_answer) VALUES (?, ?, ?, ?, ?, ?)", 
#             ("Which of the following is a sign of a phishing email?",
#              "Spelling errors", "Unusual sender", "Suspicious links", "All of the above", "All of the above"))

# cur.execute("INSERT INTO questions (question, option1, option2, option3, option4, correct_answer) VALUES (?, ?, ?, ?, ?, ?)", 
#             ("What does HTTPS mean?",
#              "HyperText Transfer Protocol Secure", "High Transfer Text Protocol", "Hidden Transfer Process", "None of these", "HyperText Transfer Protocol Secure"))

# conn.commit()
# conn.close()

# print("✅ quiz.db setup complete with sample questions!")






import sqlite3

# Connect to the database (creates file if not exists)
conn = sqlite3.connect("database/quiz.db")
cur = conn.cursor()

# Create table for quiz questions
cur.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option1 TEXT NOT NULL,
    option2 TEXT NOT NULL,
    option3 TEXT NOT NULL,
    option4 TEXT NOT NULL,
    correct_answer TEXT NOT NULL
)
""")

# Insert sample questions
sample_questions = [
    ("Which of the following is a sign of a phishing email?",
     "Spelling errors", "Unusual sender", "Suspicious links", "All of the above", "All of the above"),

    ("What does HTTPS mean?",
     "HyperText Transfer Protocol Secure", "High Transfer Text Protocol", "Hidden Transfer Process", "None of these",
     "HyperText Transfer Protocol Secure"),

    ("Which one is a safe practice online?",
     "Click random links", "Use strong passwords", "Share password with friends", "Disable antivirus",
     "Use strong passwords"),

    ("If a website asks for banking info via email, what should you do?",
     "Reply quickly", "Ignore or report it", "Send details safely", "Save as draft",
     "Ignore or report it"),

    ("What is 2FA?",
     "Two-Factor Authentication", "Two-Faced Application", "Text File Access", "None of these",
     "Two-Factor Authentication")
]

cur.executemany("INSERT INTO questions (question, option1, option2, option3, option4, correct_answer) VALUES (?, ?, ?, ?, ?, ?)",
                sample_questions)

conn.commit()
conn.close()

print("✅ quiz.db setup complete with sample questions!")
