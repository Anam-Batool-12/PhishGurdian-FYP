
# 🛡️ PhishGuardian: Rule-Based Phishing Detection and Cyber Awareness Toolkit

**PhishGuardian** is a **web-based cybersecurity awareness application** designed to detect phishing URLs using **rule-based logic** and enhance users’ cyber awareness through an **interactive quiz**.
This project was developed as a **Final Year Project (FYP)** at the **Virtual University of Pakistan**.

---

## 🚀 Project Overview

PhishGuardian empowers users to identify phishing threats and improve their cybersecurity knowledge.
It provides **real-time phishing detection**, **educational feedback**, and **visual insights** through charts — all in a **simple, responsive web interface**.

---

## ✨ Key Features

✅ **Rule-Based URL Detection** — Classifies links as *Safe*, *Suspicious*, or *Phishing*
✅ **URL Validation & Error Handling** — Prevents empty or invalid inputs
✅ **Cyber Awareness Quiz** — Engages users to test and improve their knowledge
✅ **Interactive Visualizations** — Displays results using **Chart.js** (URL scans & quiz stats)
✅ **Responsive UI** — Built with **Bootstrap** for all screen sizes
✅ **Hardware Feedback (Integrated)** — **Arduino Uno** with **LED indicators** and **Buzzer** for physical phishing alerts

---

## 🧠 Tech Stack

**Backend:** Python (Flask)
**Frontend:** HTML, CSS, Bootstrap, Chart.js
**Database:** SQLite
**Hardware Integration:** Arduino Uno, Breadboard, LEDs (Red/Green), Buzzer, Resistors, Jumper Wires

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone <repo-url>
cd PhishGuardian_FYP
```

### 2. Create a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask Application

```bash
python app.py
```

The app will run at: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 🖥️ How to Use

1. **Phishing URL Scanner:**
   → Enter a website link to check if it’s *Safe*, *Suspicious*, or *Phishing*.

2. **Cyber Awareness Quiz:**
   → Attempt the quiz to test your knowledge and receive instant feedback.

3. **Visual Reports:**
   → Analyze your results via charts for both URL scans and quiz performance.

4. **Hardware Alerts:**
   → Red LED & buzzer indicate phishing detection; green LED signals safe URLs.

---

## 🔮 Future Enhancements

* Upgrade phishing detection using **Machine Learning models**
* Add **Admin Dashboard** for monitoring and analytics
* Extend quiz database with more diverse cybersecurity topics

---

## 👨‍🏫 Supervisor

**Engr. Waqar Ahmad** — Virtual University of Pakistan

## 👩‍💻 Contributor

**Anam Batool** — Software Engineering Student, Virtual University of Pakistan

---

## 🏁 Project Status

✅ **Completed Successfully** — Final Year Project defense presented and submitted.

