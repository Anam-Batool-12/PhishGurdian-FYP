# PhishGuardian: Rule-Based Phishing Detection and Cyber Awareness Toolkit

PhishGuardian is a web-based cybersecurity awareness tool. It detects phishing URLs using rule-based logic and provides a cyber awareness quiz to educate users. This project is developed as a Final Year Project (FYP).

---

## Features

* Rule-based phishing URL detection
* Empty URL validation & error handling
* Cyber awareness quiz with score tracking
* Result visualization using Chart.js (URL scan summary & quiz performance)
* Responsive UI with Bootstrap
* Planned hardware integration with Arduino (LED + Buzzer alerts)

---

## Tech Stack

* Backend: Python (Flask)
* Frontend: HTML, CSS, Bootstrap, Chart.js
* Database: SQLite
* Hardware (Planned): Arduino Uno + LEDs + Buzzer

---

## Installation & Setup

### 1. Clone the repository

```
git clone <repo-url>
cd PhishGuardian_FYP
```

### 2. Create a virtual environment

```
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run the Flask app

```
python app.py
```

App will be available at: `http://127.0.0.1:5000`

---

## Usage

1. **URL Scanner**: Enter a URL → classified as Safe, Suspicious, or Phishing.
2. **Cyber Awareness Quiz**: Take the quiz → get your score & feedback.
3. **Charts & Reports**: Visualize results:

   * URL scan summary (Safe vs Phishing count)
   * Quiz performance (score breakdown)

---

## Future Scope

* Arduino integration (Red/Green LEDs + buzzer) for physical feedback during phishing detection.
* Expand detection logic with Machine Learning.
* Admin dashboard for user activity reports.

---

## Contributor

Anam Batool – Software Engineering Student, Virtual University of Pakistan
