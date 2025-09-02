from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecret"

# ---------- DB SETUP ----------
DB_PATH = os.path.join("database", "phishguardian.db")
os.makedirs("database", exist_ok=True)

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# ---------- URL CHECK ----------
def is_phishing_url(url: str) -> bool:
    suspicious_keywords = ["login", "verify", "update", "bank", "secure", "confirm"]
    suspicious_exts = [".exe", ".scr", ".zip"]

    if not url or url.strip() == "":
        return None

    if any(keyword in url.lower() for keyword in suspicious_keywords):
        return True
    if any(url.lower().endswith(ext) for ext in suspicious_exts):
        return True
    return False


# ---------- ROUTES ----------
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/check_url", methods=["GET", "POST"])
def check_url():
    result = None
    is_phish = False

    if request.method == "POST":
        url = request.form.get("url")
        phish_check = is_phishing_url(url)

        if phish_check is None:
            result = "URL is required"
        elif phish_check:
            result = "⚠️ Phishing URL detected!"
            is_phish = True
        else:
            result = "✅ Safe URL"

        # Save in session logs
        if "logs" not in session:
            session["logs"] = []
        session["logs"].append({"url": url, "result": result})

        # Save in DB
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO url_logs (url, result, checked_at) VALUES (?, ?, ?)",
            (url, result, datetime.now()),
        )
        conn.commit()
        conn.close()

    return render_template("check_url.html", result=result, is_phish=is_phish)


# ---------- RESULTS ----------
@app.route("/results")
def results():
    session_logs = session.get("logs", [])
    conn = get_db_connection()
    db_logs = conn.execute(
        "SELECT * FROM url_logs ORDER BY checked_at DESC LIMIT 20"
    ).fetchall()
    conn.close()
    return render_template("results.html", session_logs=session_logs, db_logs=db_logs)


# ---------- QUIZ ----------
QUESTIONS = [
    {"id": 1, "q": "Which is safer?", "options": ["http://bank.com", "https://bank.com"], "answer": "B"},
    {"id": 2, "q": "What should you avoid clicking?", "options": ["Unknown links", "Official site"], "answer": "A"},
    {"id": 3, "q": "Phishing usually asks for?", "options": ["Personal info", "Weather updates"], "answer": "A"},
]

@app.route("/quiz")
def quiz():
    return render_template("quiz.html", questions=QUESTIONS)

@app.route("/submit_quiz", methods=["POST"])
def submit_quiz():
    score, total, skipped = 0, len(QUESTIONS), 0
    for q in QUESTIONS:
        answer = request.form.get(f"question_{q['id']}")
        if not answer:
            skipped += 1
        elif answer == q["answer"]:
            score += 1

    # Save stats for Chart.js
    session["last_score"] = score
    session["last_total"] = total
    session["last_skipped"] = skipped

    return render_template("quiz_result.html", score=score, total=total, skipped=skipped)


# ---------- CHART ENDPOINTS ----------
@app.route("/chart/url_summary")
def chart_url_summary():
    conn = get_db_connection()
    data = conn.execute("SELECT result, COUNT(*) as count FROM url_logs GROUP BY result").fetchall()
    conn.close()
    summary = {"safe": 0, "phishing": 0}
    for row in data:
        if "Safe" in row["result"]:
            summary["safe"] = row["count"]
        elif "Phishing" in row["result"]:
            summary["phishing"] = row["count"]
    return jsonify(summary)

@app.route("/chart/quiz_summary")
def chart_quiz_summary():
    return jsonify(
        {
            "score": session.get("last_score", 0),
            "total": session.get("last_total", 0),
            "skipped": session.get("last_skipped", 0),
        }
    )

if __name__ == "__main__":
    app.run(debug=True)
