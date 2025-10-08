from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import sqlite3
import os
from datetime import datetime
import serial
import time

# Import hardware + phishing rules
from hardware import indicate_url_status
from phishing_rules.rules import is_phishy

# ---------- ARDUINO SETUP ----------
# Try connecting once (optional first check)
try:
    arduino = serial.Serial('COM4', 9600, timeout=1)
    time.sleep(2)  # wait for Arduino to reset
    print("✅ Arduino connected successfully on COM4!")
    arduino.close()
except Exception as e:
    arduino = None
    print("⚠️ Arduino not found:", e)


# ---------- FLASK APP ----------
app = Flask(__name__)
app.secret_key = "superscret"

# ---------- DATABASE SETUP ----------
DB_PATH = os.path.join("database", "phishguardian.db")
os.makedirs("database", exist_ok=True)

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# ---------- ROUTES ----------
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/check_url", methods=["GET", "POST"])
def check_url():
    result = None
    is_phish = False
    hardware_feedback = None

    if request.method == "POST":
        url = request.form.get("url")

        # --- Run rule-based detection ---
        phish_check, reason = is_phishy(url)

        if phish_check:
            result = f"Phishing URL detected! ({reason})"
            is_phish = True
        else:
            result = reason  # e.g., "This URL seems safe."

        # --- Hardware LED text feedback ---
        status = "phishing" if is_phish else "safe"
        hardware_feedback = indicate_url_status(status)

        # --- ✅ Send signal to Arduino ---
        try:
            arduino = serial.Serial('COM4', 9600, timeout=1)
            time.sleep(2)  # let Arduino get ready

            if is_phish:
                arduino.write(b"PHISH\n")
                print("🔴 Sent to Arduino: PHISH")
            else:
                arduino.write(b"SAFE\n")
                print("🟢 Sent to Arduino: SAFE")

            arduino.close()
        except Exception as e:
            print("⚠️ Arduino write error:", e)

        # --- Save in session (for quick access) ---
        if "logs" not in session:
            session["logs"] = []
        session["logs"].append({"url": url, "result": result})

        # --- Save in Database ---
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO url_logs (url, result, checked_at) VALUES (?, ?, ?)",
            (url, result, datetime.now()),
        )
        conn.commit()
        conn.close()

    return render_template(
        "check_url.html",
        result=result,
        is_phish=is_phish,
        feedback=hardware_feedback,
    )


# ---------- RESULTS PAGE ----------
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
    score = 0
    total = len(QUESTIONS)

    for q in QUESTIONS:
        answer = request.form.get(f"question_{q['id']}")
        if answer == q["answer"]:
            score += 1

    # Save stats for Chart.js
    session["last_score"] = score
    session["last_total"] = total

    return render_template("quiz_result.html", score=score, total=total)


# ---------- CHART API (for Chart.js) ----------
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


# ---------- MAIN ----------
if __name__ == "__main__":
    app.run(debug=True)
