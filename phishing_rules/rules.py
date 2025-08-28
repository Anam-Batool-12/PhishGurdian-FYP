import re

def is_phishy(url):
    # Rule 1: No HTTPS
    if url.startswith("http://"):
        return True, "URL is not secure (uses http instead of https)."

    # Rule 2: Suspicious keywords
    suspicious_keywords = ["login", "verify", "update", "secure", "free", "click", "account", "bank", "confirm"]
    for keyword in suspicious_keywords:
        if keyword in url.lower():
            return True, f"Suspicious keyword found: {keyword}"

    # Rule 3: Long URL
    if len(url) > 75:
        return True, "URL is too long, looks suspicious."

    # Rule 4: Too many dots
    if url.count(".") > 3:
        return True, "URL has too many subdomains."

    # Rule 5: Numbers in domain
    domain = url.split("//")[-1].split("/")[0]
    if any(char.isdigit() for char in domain):
        return True, "Domain name contains numbers, looks suspicious."

    # Rule 6: Special characters
    if re.search(r"[@\-_%=]", domain):
        return True, "Domain contains unusual special characters."

    # Rule 7: IP Address instead of domain
    if re.match(r"^https?:\/\/\d+\.\d+\.\d+\.\d+", url):
        return True, "URL is using an IP address instead of domain name."

    return False, "✅ This URL seems safe."
