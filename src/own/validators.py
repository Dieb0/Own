"""Data validation utilities."""

import re


def is_valid_email(email: str) -> bool:
    """Check if the given string is a valid email address (basic check)."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def is_valid_url(url: str) -> bool:
    """Check if the given string is a valid URL (basic check)."""
    pattern = r"^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$"
    return bool(re.match(pattern, url))


def is_valid_ipv4(ip: str) -> bool:
    """Check if the given string is a valid IPv4 address."""
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        num = int(part)
        if num < 0 or num > 255:
            return False
        if len(part) > 1 and part[0] == "0":
            return False
    return True


def is_strong_password(password: str) -> bool:
    """Check if password is strong (8+ chars, upper, lower, digit, special)."""
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True


def is_valid_phone(phone: str) -> bool:
    """Check if a string is a valid phone number (US format)."""
    pattern = r"^(\+1)?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$"
    return bool(re.match(pattern, phone))


def is_valid_hex_color(color: str) -> bool:
    """Check if the given string is a valid hex color code."""
    pattern = r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"
    return bool(re.match(pattern, color))


def is_valid_credit_card(number: str) -> bool:
    """Validate a credit card number using the Luhn algorithm."""
    digits = number.replace(" ", "").replace("-", "")
    if not digits.isdigit() or len(digits) < 13 or len(digits) > 19:
        return False
    total = 0
    reverse_digits = digits[::-1]
    for i, d in enumerate(reverse_digits):
        n = int(d)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0
