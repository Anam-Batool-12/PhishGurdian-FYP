import re

def is_phishy(url):
    if not url or not isinstance(url, str) or url.strip() == "":
        return True, "Empty or missing URL"

    url = url.strip().lower()

    if not re.match(r"^(https?:\/\/)?([\w\-]+\.)+[\w\-]+(\/.*)?$", url):
        return True, "Malformed URL structure"

    if url.startswith("http://"):
        return True, "Uses insecure HTTP"

    suspicious_keywords = [
        "login", "verify", "update", "secure",
        "account", "bank", "confirm", "signin", "free", "click"
    ]

    for keyword in suspicious_keywords:
        if keyword in url:
            return True, f"Suspicious keyword detected: {keyword}"

    if len(url) > 75:
        return True, "URL length is unusually long"

    if url.count(".") > 3:
        return True, "Too many subdomains"

    domain = url.split("//")[-1].split("/")[0]

    # IP-based URL
    if re.match(r"\d+\.\d+\.\d+\.\d+", domain):
        return True, "IP-based URL detected"

    if re.search(r"[@_%=]", domain):
        return True, "Unusual characters in domain"

    return False, "No phishing indicators found"
