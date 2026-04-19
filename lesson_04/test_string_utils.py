import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize('input_str, expected', [
    ('привет', 'Привет'),
    ('hellow world!', 'Hellow world!'),
    ('день 1', 'День 1'),
    ('0ABC', '0abc'),
    ('  ', '  '),
    (' abc', ' abc'),
    ('False', 'False'),
    ('[1, 2]', '[1, 2]')
    ])
def test_positive_capitalize(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
def test_positive_capitalize_bool():
    string_utils = StringUtils()
    res = string_utils.capitalize('')
    assert res == ''
    assert len(res) == 0


@pytest.mark.negative
def test_negative_capitalize_type():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.capitalize(1)


@pytest.mark.negative
def test_negative_capitalize_list():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.capitalize([1, 2])


@pytest.mark.positive
@pytest.mark.parametrize('string', [
    (' Hellow'), (' _hellow world!'), (' 1!@'), ('False'), ('[1, 2]')])
def test_positive_trim(string):
    string_utils = StringUtils()
    res = string_utils.trim(string)
    assert res


@pytest.mark.negative
@pytest.mark.parametrize('input_str, expected', [('   ', ''), ('', '')])
def test_negative_trim_None(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
def test_negative_trim_none():
    with pytest.raises(AttributeError):
        string_utils.trim(None)


@pytest.mark.positive
@pytest.mark.parametrize('string, symbol, expected', [
    ('abc', 'a', True),
    ('123', '2', True),
    ('!@_', '_', True),
    ('test', 'test'[0], True),
    ('test', 'test'[-1], True),
    ('abc', 'd', False)
    ])
def test_positive_contains(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize('input_str, input_symbol, expected', [
    ('test', 'testic', False), ('test', '', True)])
def test_negative_contains_None(input_str, input_symbol, expected):
    assert string_utils.contains(input_str, input_symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize('string, symbol, expected', [
    ('test', 't', 'es'),
    ('test', 'e', 'tst'),
    ('test', '', 'test'),
    ('test', '1', 'test'),
    ('test', 'test'[1], 'tst'),
    ('  ', 't', '  ')
    ])
def test_positive_delete_symbol(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
def test_delete_symbol_empty_string():
    string_utils = StringUtils()
    res = string_utils.delete_symbol('', 't')
    assert res == ''
