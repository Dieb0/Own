"""Tests for calculator module."""

import pytest

from own.calculator import (
    add,
    divide,
    factorial,
    fibonacci,
    modulo,
    multiply,
    power,
    subtract,
)


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 100) == 0
    assert multiply(-2, 3) == -6


def test_divide():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(1, 0)


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(2, -1) == 0.5


def test_modulo():
    assert modulo(10, 3) == 1
    assert modulo(9, 3) == 0


def test_modulo_by_zero():
    with pytest.raises(ZeroDivisionError, match="zero divisor"):
        modulo(5, 0)


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800


def test_factorial_negative():
    with pytest.raises(ValueError, match="negative"):
        factorial(-1)


def test_fibonacci():
    assert fibonacci(0) == []
    assert fibonacci(1) == [0]
    assert fibonacci(2) == [0, 1]
    assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]


def test_fibonacci_negative():
    with pytest.raises(ValueError, match="non-negative"):
        fibonacci(-1)
