"""Tests for string_utils module."""

import pytest

from own.string_utils import (
    camel_to_snake,
    capitalize_words,
    count_consonants,
    count_vowels,
    is_palindrome,
    remove_duplicates,
    reverse,
    snake_to_camel,
    truncate,
)


def test_reverse():
    assert reverse("hello") == "olleh"
    assert reverse("") == ""
    assert reverse("a") == "a"


def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("A man a plan a canal Panama") is True
    assert is_palindrome("") is True


def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("python") == "Python"
    assert capitalize_words("") == ""


def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("AEIOU") == 5
    assert count_vowels("xyz") == 0
    assert count_vowels("") == 0


def test_count_consonants():
    assert count_consonants("hello") == 3
    assert count_consonants("aeiou") == 0
    assert count_consonants("bcdfg") == 5
    assert count_consonants("") == 0


def test_truncate():
    assert truncate("hello world", 20) == "hello world"
    assert truncate("hello world", 8) == "hello..."
    assert truncate("hello world", 5) == "he..."


def test_truncate_custom_suffix():
    assert truncate("hello world", 6, suffix="~") == "hello~"


def test_truncate_invalid_max_length():
    with pytest.raises(ValueError, match="max_length"):
        truncate("hello", 2, suffix="...")


def test_snake_to_camel():
    assert snake_to_camel("hello_world") == "helloWorld"
    assert snake_to_camel("one_two_three") == "oneTwoThree"
    assert snake_to_camel("single") == "single"


def test_camel_to_snake():
    assert camel_to_snake("helloWorld") == "hello_world"
    assert camel_to_snake("oneTwoThree") == "one_two_three"
    assert camel_to_snake("single") == "single"


def test_remove_duplicates():
    assert remove_duplicates("aabbcc") == "abc"
    assert remove_duplicates("hello") == "helo"
    assert remove_duplicates("") == ""
    assert remove_duplicates("a") == "a"
