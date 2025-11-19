import re

def is_phishy(url):
    if not url or not isinstance(url, str) or url.strip() == "":
        return False, "URL is required."

    if not re.match(r"^(https?:\/\/)?([\w\-]+\.)+[\w\-]+(\/.*)?$", url):
        return False, "Invalid URL format."

    if url.startswith("http://"):
        return True, "URL is not secure (uses http instead of https)."

    suspicious_keywords = ["login", "verify", "update", "secure", "free", "click", "account", "bank", "confirm"]
    for keyword in suspicious_keywords:
        if keyword in url.lower():
            return True, f"Suspicious keyword found: {keyword}"

    if len(url) > 75:
        return True, "URL is too long, looks suspicious."

    if url.count(".") > 3:
        return True, "URL has too many subdomains."

    domain = url.split("//")[-1].split("/")[0]
    if any(char.isdigit() for char in domain):
        return True, "Domain name contains numbers, looks suspicious."

    if re.search(r"[@\-_%=]", domain):
        return True, "Domain contains unusual special characters."

    if re.match(r"^https?:\/\/\d+\.\d+\.\d+\.\d+", url):
        return True, "URL is using an IP address instead of domain name."

    return False, "This URL seems safe."




