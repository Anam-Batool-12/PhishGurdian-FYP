# hardware_sim.py
"""
Simulated hardware integration for PhishGuardian.
Mimics Arduino behavior with LEDs and buzzer.
"""

def indicate_url_status(url_status: str):
    """
    Simulates LED and buzzer feedback.
    url_status: 'safe' or 'phishing'
    """
    if url_status.lower() == 'phishing':
        message = "[RED LED ON] [GREEN LED OFF] [BUZZER ON]"
    elif url_status.lower() == 'safe':
        message = "[GREEN LED ON] [RED LED OFF] [BUZZER OFF]"
    else:
        message = "[ERROR] Unknown status"

    # Print to console (simulate hardware activity)
    print("Hardware Simulation:", message)
    return message
