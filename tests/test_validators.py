"""Tests for validators module."""

from own.validators import (
    is_strong_password,
    is_valid_credit_card,
    is_valid_email,
    is_valid_hex_color,
    is_valid_ipv4,
    is_valid_phone,
    is_valid_url,
)


class TestEmail:
    def test_valid_emails(self):
        assert is_valid_email("user@example.com") is True
        assert is_valid_email("first.last@domain.org") is True
        assert is_valid_email("user+tag@sub.domain.co") is True

    def test_invalid_emails(self):
        assert is_valid_email("") is False
        assert is_valid_email("noatsign.com") is False
        assert is_valid_email("@nodomain.com") is False
        assert is_valid_email("user@") is False
        assert is_valid_email("user@.com") is False


class TestUrl:
    def test_valid_urls(self):
        assert is_valid_url("http://example.com") is True
        assert is_valid_url("https://www.example.org") is True
        assert is_valid_url("https://sub.domain.co/path") is True

    def test_invalid_urls(self):
        assert is_valid_url("") is False
        assert is_valid_url("ftp://example.com") is False
        assert is_valid_url("example.com") is False
        assert is_valid_url("http://") is False


class TestIPv4:
    def test_valid_ipv4(self):
        assert is_valid_ipv4("192.168.1.1") is True
        assert is_valid_ipv4("0.0.0.0") is True
        assert is_valid_ipv4("255.255.255.255") is True

    def test_invalid_ipv4(self):
        assert is_valid_ipv4("") is False
        assert is_valid_ipv4("256.1.1.1") is False
        assert is_valid_ipv4("1.2.3") is False
        assert is_valid_ipv4("1.2.3.4.5") is False
        assert is_valid_ipv4("01.02.03.04") is False
        assert is_valid_ipv4("abc.def.ghi.jkl") is False


class TestPassword:
    def test_strong_passwords(self):
        assert is_strong_password("Str0ng!Pass") is True
        assert is_strong_password("Abcdef1!") is True

    def test_weak_passwords(self):
        assert is_strong_password("short1!") is False  # too short
        assert is_strong_password("nouppercase1!") is False
        assert is_strong_password("NOLOWERCASE1!") is False
        assert is_strong_password("NoDigits!!") is False
        assert is_strong_password("NoSpecial1") is False


class TestPhone:
    def test_valid_phones(self):
        assert is_valid_phone("555-123-4567") is True
        assert is_valid_phone("(555) 123-4567") is True
        assert is_valid_phone("+1 555 123 4567") is True
        assert is_valid_phone("5551234567") is True

    def test_invalid_phones(self):
        assert is_valid_phone("") is False
        assert is_valid_phone("123") is False
        assert is_valid_phone("abcdefghij") is False


class TestHexColor:
    def test_valid_hex_colors(self):
        assert is_valid_hex_color("#fff") is True
        assert is_valid_hex_color("#FFF") is True
        assert is_valid_hex_color("#ff0000") is True
        assert is_valid_hex_color("#A1B2C3") is True

    def test_invalid_hex_colors(self):
        assert is_valid_hex_color("") is False
        assert is_valid_hex_color("#gg0000") is False
        assert is_valid_hex_color("ff0000") is False
        assert is_valid_hex_color("#ffff") is False


class TestCreditCard:
    def test_valid_credit_cards(self):
        # Luhn-valid test numbers
        assert is_valid_credit_card("4111111111111111") is True
        assert is_valid_credit_card("4111 1111 1111 1111") is True
        assert is_valid_credit_card("5500-0000-0000-0004") is True

    def test_invalid_credit_cards(self):
        assert is_valid_credit_card("") is False
        assert is_valid_credit_card("1234567890123456") is False
        assert is_valid_credit_card("123") is False
        assert is_valid_credit_card("abcdefghijklmnop") is False
