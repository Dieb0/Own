"""Unit conversion and data format conversion utilities."""


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def km_to_miles(km: float) -> float:
    """Convert kilometers to miles."""
    return km * 0.621371


def miles_to_km(miles: float) -> float:
    """Convert miles to kilometers."""
    return miles / 0.621371


def kg_to_pounds(kg: float) -> float:
    """Convert kilograms to pounds."""
    return kg * 2.20462


def pounds_to_kg(pounds: float) -> float:
    """Convert pounds to kilograms."""
    return pounds / 2.20462


def decimal_to_binary(n: int) -> str:
    """Convert a non-negative integer to its binary string representation.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Only non-negative integers are supported")
    if n == 0:
        return "0"
    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n //= 2
    return "".join(reversed(bits))


def binary_to_decimal(binary: str) -> int:
    """Convert a binary string to a decimal integer.

    Raises:
        ValueError: If binary contains invalid characters.
    """
    if not all(c in "01" for c in binary):
        raise ValueError("Invalid binary string")
    return int(binary, 2)


def hex_to_decimal(hex_str: str) -> int:
    """Convert a hexadecimal string to a decimal integer.

    Raises:
        ValueError: If hex_str contains invalid characters.
    """
    try:
        return int(hex_str, 16)
    except ValueError:
        raise ValueError(f"Invalid hexadecimal string: {hex_str}")


def decimal_to_hex(n: int) -> str:
    """Convert a non-negative integer to a hexadecimal string.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Only non-negative integers are supported")
    return hex(n)[2:]


def liters_to_gallons(liters: float) -> float:
    """Convert liters to US gallons."""
    return liters * 0.264172


def gallons_to_liters(gallons: float) -> float:
    """Convert US gallons to liters."""
    return gallons / 0.264172
