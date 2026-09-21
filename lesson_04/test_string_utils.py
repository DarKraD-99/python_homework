import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("school", "School"),
    ("hello world", "Hello world"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),
    ("    School", "School"),
    ("No space", "No space"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, sym_str, expected", [
    ("SkyPro", "S", True),
    ("Letter", "e", True),
    ("Car", "C", True),
])
def test_contains_positive(input_str, sym_str, expected):
    assert string_utils.contains(input_str, sym_str) == expected


@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, sym_str, expected", [
    ("SkyPro", "S", "kyPro"),
    ("Walk", "Wa", "lk"),
    ("Hand", "Hand", ""),
])
def test_delete_positive(input_str, sym_str, expected):
    assert string_utils.delete_symbol(input_str, sym_str) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("input_str, expected", [
    ("tABLE", "Table"),  # Понижает регистр остальных букв после первой
    (" ", " "),
    ("123word", "123word"),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("input_str, expected", [
    (" Delete ", "Delete "),
    ("   ", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("input_str, sym_str, expected", [
    ("Candy", "X", False),
    ("Love", "", True),  # Должен возвращать False
    ("SkyPro", "s", False),
])
def test_contains_negative(input_str, sym_str, expected):
    assert string_utils.contains(input_str, sym_str) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("input_str, sym_str, expected", [
    ("Guitare", "eratiuG", "Guitare"),
    ("Water", "L", "Water"),
])
def test_delete_negative(input_str, sym_str, expected):
    assert string_utils.delete_symbol(input_str, sym_str) == expected
