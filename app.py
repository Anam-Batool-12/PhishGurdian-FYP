from flask import Flask, render_template, request
import sqlite3
from phishing_rules.rules import is_phishy  # rule-based detection

app = Flask(__name__)

# ---------------------------
# QUIZ HELPER FUNCTIONS
# ---------------------------
def get_quiz_questions(limit=5):
    """Fetch random quiz questions from the DB."""
    conn = sqlite3.connect("database/quiz.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM questions ORDER BY RANDOM() LIMIT ?", (limit,))
    questions = cur.fetchall()
    conn.close()
    return questions


# ---------------------------
# ROUTES
# ---------------------------

@app.route("/")
def index():
    return render_template("index.html")


# URL Checker page
@app.route("/check_url", methods=["GET", "POST"])
def check_url():
    result_message = None
    is_phish = None

    if request.method == "POST":
        url = request.form["url"]
        is_phish, message = is_phishy(url)  # returns (True/False, message)
        result_message = message

        # Save to log DB
        conn = sqlite3.connect("database/quiz.db")
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO url_logs (url, is_phishing, result) VALUES (?, ?, ?)",
            (url, 1 if is_phish else 0, message),
        )
        conn.commit()
        conn.close()

    return render_template("check_url.html", result=result_message, is_phish=is_phish)


# Quiz page
@app.route("/quiz")
def quiz():
    questions = get_quiz_questions()
    return render_template("quiz.html", questions=questions)


# Quiz submission → quiz_results.html
@app.route("/submit_quiz", methods=["POST"])
def submit_quiz():
    score = 0
    total = 0
    skipped = 0

    conn = sqlite3.connect("database/quiz.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM questions")
    all_questions = cur.fetchall()
    conn.close()

    # Loop through DB questions to check answers
    for q in all_questions:
        qid = str(q["id"])  # question ID
        correct_answer = q["correct_option"]  # A / B / C / D
        user_answer = request.form.get(f"question_{qid}")

        total += 1
        if user_answer:
            if user_answer == correct_answer:
                score += 1
        else:
            skipped += 1

    return render_template(
        "quiz_result.html", score=score, total=total, skipped=skipped
    )


# Results page → show last 10 URL logs
@app.route("/results")
def results():
    conn = sqlite3.connect("database/quiz.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM url_logs ORDER BY checked_at DESC LIMIT 10")
    logs = cur.fetchall()
    conn.close()

    return render_template("results.html", logs=logs)


# ---------------------------
# MAIN
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True)
