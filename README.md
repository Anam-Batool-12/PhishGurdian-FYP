#  PhishGuardian: Rule-Based Phishing Detection & Cyber Awareness Toolkit

**PhishGuardian** is a **web-based cybersecurity awareness platform** built to detect phishing URLs using **rule-based logic** and boost users’ cyber hygiene through an **interactive quiz**.
This project was developed as a **Final Year Project (FYP)** at the **Virtual University of Pakistan**.

##  Project Overview

PhishGuardian helps users spot shady URLs & level up their cybersecurity vibes.
It offers **real-time detection**, **instant explanations**, **visual insights**, and even **hardware-based alerts** using an **Arduino Uno**.


## Key Features

✅ **Rule-Based URL Detection** → Categorizes URLs as *Safe*,  or *Phishing*
✅ **Smart Validation** → Blocks empty/invalid inputs
✅ **Cyber Awareness Quiz** → Quick, interactive, and beginner-friendly
✅ **Charts & Analytics** → Quiz and scan stats powered by **Chart.js**
✅ **Responsive Design** → Built using **Bootstrap**
✅ **Hardware Alerts** → Arduino LEDs + Buzzer react to URL status in real time


## Tech Stack

**Backend:** Python (Flask)
**Frontend:** HTML, CSS, Bootstrap, Chart.js
**Database:** SQLite
**Hardware:** Arduino Uno, Breadboard, LEDs (Red/Green), Resistors, Buzzer, Jumper Wires

##  Installation & Setup

### 1. Clone the Repo

```bash
git clone <repo-url>
cd PhishGuardian_FYP
```

### 2. Create the Virtual Environment

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

### 4. Run the Flask App

```bash
python app.py
```

App opens at: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

#  How to Run the Arduino Code

### Requirements

* Arduino Uno
* USB cable
* Arduino IDE (from arduino.cc)
* Your Arduino `.ino` code file
* Connected hardware:

  * Red LED (with resistor)
  * Green LED (with resistor)
  * Buzzer
  * Jumper wires + breadboard


### 1. Open the Arduino Code

1. Launch **Arduino IDE**
2. Go to **File → Open**
3. Select your `phishguardian.ino` (or whatever you named it)


### 2. Select Your Board & Port

* Go to **Tools → Board → Arduino Uno**
* Go to **Tools → Port → COMX** (Windows) or `/dev/ttyUSBX` (Linux/Mac)

If you're unsure which COM port it is… just unplug → see which one disappears → plug back.

---

###  3. Upload the Code

Simply hit the **Upload (→)** button.
The IDE will compile + flash the code onto your Arduino.

If it says *Done Uploading* → your board is good to go 



### 4. Ensure Serial Communication Works

* Arduino should use **9600 baud rate**
* In your code:

  ```cpp
  Serial.begin(9600);
  ```
* Python side should match this in your `serial.Serial()` config.



### 🟩🟥 5. Hardware Behavior

Once connected to your Flask backend:

| URL Result | Green LED   | Red LED     | Buzzer        |
| ---------- | ----------- | ----------- | ------------- |
| Safe       | Blinks 2–3x | Off         | Silent        |
| Suspicious | Off         | Blinks      | Optional beep |
| Phishing   | Off         | Blinks 2–3x | Beeps         |

You can customize blink count, timing, or buzzer style inside the `.ino` logic.


#  Future Enhancements

* Add **machine learning–based detection**
* Advanced **admin dashboard**
* Bigger, more diverse **quiz question bank**


##  Supervisor

**Engr. Waqar Ahmad** — Virtual University of Pakistan

## Contributor

**Anam Batool** — Software Engineering Student, VU


## 🏁 Project Status

✅ **Successfully Completed** — Fully developed, presented, and submitted.



