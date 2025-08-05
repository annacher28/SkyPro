import pytest
from string_utils import StringUtils


string_utils = StringUtils()

print('start')

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),       # Удаляет пробелы
    ("skypro", "skypro"),          # Без пробелов → без изменений
    ("    hello", "hello"),        # Множественные пробелы
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),                      # Пустая строка
    ("   ", ""),                   # Только пробелы → должна вернуться пустая строка
    ("  a  ", "a  "),              # Пробелы только в начале
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),         # Символ есть
    ("SkyPro", "U", False),        # Символа нет
    ("Hello", "l", True),          # Символ встречается несколько раз
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("", "a", False),              # Пустая строка
    ("SkyPro", "", False),         # Пустой символ
    ("   ", " ", True),            # Строка из пробелов, ищем пробел
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),      # Удаление одного символа
    ("SkyPro", "Pro", "Sky"),      # Удаление подстроки
    ("Hello", "l", "Heo"),         # Удаление всех вхождений
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("", "a", ""),                 # Пустая строка
    ("SkyPro", "Z", "SkyPro"),     # Символ не найден → строка без изменений
    ("   ", " ", ""),              # Удаление всех пробелов
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected





print('finish')