"""Tests for converters module."""

import pytest

from own.converters import (
    binary_to_decimal,
    celsius_to_fahrenheit,
    decimal_to_binary,
    decimal_to_hex,
    fahrenheit_to_celsius,
    gallons_to_liters,
    hex_to_decimal,
    kg_to_pounds,
    km_to_miles,
    liters_to_gallons,
    miles_to_km,
    pounds_to_kg,
)


class TestTemperature:
    def test_celsius_to_fahrenheit_freezing(self):
        assert celsius_to_fahrenheit(0) == 32

    def test_celsius_to_fahrenheit_boiling(self):
        assert celsius_to_fahrenheit(100) == 212

    def test_celsius_to_fahrenheit_negative(self):
        assert celsius_to_fahrenheit(-40) == -40

    def test_fahrenheit_to_celsius_freezing(self):
        assert fahrenheit_to_celsius(32) == 0

    def test_fahrenheit_to_celsius_boiling(self):
        assert fahrenheit_to_celsius(212) == 100

    def test_fahrenheit_to_celsius_negative(self):
        assert fahrenheit_to_celsius(-40) == -40


class TestDistance:
    def test_km_to_miles(self):
        assert abs(km_to_miles(1) - 0.621371) < 0.0001

    def test_km_to_miles_zero(self):
        assert km_to_miles(0) == 0

    def test_miles_to_km(self):
        assert abs(miles_to_km(1) - 1.60934) < 0.001

    def test_miles_to_km_zero(self):
        assert miles_to_km(0) == 0

    def test_roundtrip_km_miles(self):
        assert abs(miles_to_km(km_to_miles(10)) - 10) < 0.001


class TestWeight:
    def test_kg_to_pounds(self):
        assert abs(kg_to_pounds(1) - 2.20462) < 0.0001

    def test_kg_to_pounds_zero(self):
        assert kg_to_pounds(0) == 0

    def test_pounds_to_kg(self):
        assert abs(pounds_to_kg(1) - 0.45359) < 0.001

    def test_roundtrip_kg_pounds(self):
        assert abs(pounds_to_kg(kg_to_pounds(5)) - 5) < 0.001


class TestBinary:
    def test_decimal_to_binary_zero(self):
        assert decimal_to_binary(0) == "0"

    def test_decimal_to_binary_positive(self):
        assert decimal_to_binary(10) == "1010"
        assert decimal_to_binary(1) == "1"
        assert decimal_to_binary(255) == "11111111"

    def test_decimal_to_binary_negative_raises(self):
        with pytest.raises(ValueError, match="non-negative"):
            decimal_to_binary(-1)

    def test_binary_to_decimal(self):
        assert binary_to_decimal("1010") == 10
        assert binary_to_decimal("0") == 0
        assert binary_to_decimal("11111111") == 255

    def test_binary_to_decimal_invalid_raises(self):
        with pytest.raises(ValueError, match="Invalid binary"):
            binary_to_decimal("102")


class TestHexadecimal:
    def test_hex_to_decimal(self):
        assert hex_to_decimal("a") == 10
        assert hex_to_decimal("ff") == 255
        assert hex_to_decimal("0") == 0

    def test_hex_to_decimal_invalid_raises(self):
        with pytest.raises(ValueError, match="Invalid hexadecimal"):
            hex_to_decimal("xyz")

    def test_decimal_to_hex(self):
        assert decimal_to_hex(10) == "a"
        assert decimal_to_hex(255) == "ff"
        assert decimal_to_hex(0) == "0"

    def test_decimal_to_hex_negative_raises(self):
        with pytest.raises(ValueError, match="non-negative"):
            decimal_to_hex(-1)


class TestVolume:
    def test_liters_to_gallons(self):
        assert abs(liters_to_gallons(1) - 0.264172) < 0.0001

    def test_liters_to_gallons_zero(self):
        assert liters_to_gallons(0) == 0

    def test_gallons_to_liters(self):
        assert abs(gallons_to_liters(1) - 3.78541) < 0.001

    def test_roundtrip_liters_gallons(self):
        assert abs(gallons_to_liters(liters_to_gallons(10)) - 10) < 0.001
