import pytest

from exercise import reverse_string


def test_reverse_regular():
    assert reverse_string("hello") == "olleh"


def test_reverse_empty():
    assert reverse_string("") == ""


def test_reverse_single_char():
    assert reverse_string("a") == "a"


def test_reverse_palindrome():
    assert reverse_string("racecar") == "racecar"


def test_reverse_with_spaces():
    assert reverse_string("hello world") == "dlrow olleh"


def test_reverse_unicode():
    assert reverse_string("ñá🙂") == "🙂áñ"


def test_reverse_non_string_raises():
    with pytest.raises(TypeError):
        reverse_string(None)
