from string_utils import StringUtils


import pytest


utils = StringUtils()

capitilize_pozitive_list = [
                 ("skypro", "Skypro"),
                 ("SKYPRO", "Skypro"),
                 ("Skypro", "Skypro"),
                 ("skypro is cool", "Skypro is cool")
                ]

capitilize_negative_list = [
                 (" skypro", " skypro"),
                 ("12Skypro", "12skypro"),
                 ("12345", "12345"),
                 ("-Skypro", "-skypro"),
                 ("@skyPro", "@skypro"),
                 ("يولد جميع الناس أحراراً", "يولد جميع الناس أحراراً"),
                 ("", ""),
                 (" ", " "),
                 (None, "")
                ]

trim_pozitive_list = [
                          (" Skypro", "Skypro"),
                          ("          Skypro", "Skypro"),
                          (" Skypro  ", "Skypro  "),
                          ("     in Skypro", "in Skypro")
                         ]

trim_negative_list = [
                      ("", ""),
                      (" ", ""),
                      ("           ", ""),
                      ("    -    ", "-    "),
                      (None, None)
                     ]

to_list_pozitive_list = [
                         ("a,b,c,d", ",", ["a", "b", "c", "d"]),
                         ("1:2:3", ":", ["1", "2", "3"]),
                         ("1 2 3 4 5 6 7 8 9", " ",
                          ['1', '2', '3', '4', '5', '6', '7', '8', '9'])
                        ]

to_list_negative_list = [
                         ("a,b,c,d", "-", ["a,b,c,d"]),
                         ("Привет!", ",", ["Привет!"]),
                         ("a,b,c,d", None, ["a,b,c,d"]),
                         ("", None, []),
                         (None, None, [])
                        ]

contains_pozitive_list = [
                          ("Skypro", "S", True),
                          ("Skypro", "U", False),
                          ("Привет, как дела?", "?", True),
                          ("Привет, как дела?", " ", True)
                         ]

contains_negative_list = [
                          ("Skypro", "s", True),
                          ("Skypro", "", False),
                          ("Skypro", None, False),
                          ("Skypro", "Sky", False)
                         ]

delete_simbol_pozitive_list = [
                               ("SkyproS", "S", "kypro"),
                               ("Skypro", "k", "Sypro")
                              ]

delete_simbol_negative_list = [
                               ("Skypro", None, "Skypro"),
                               ("Skypro", " ", "Skypro"),
                               ("Skypro", "", "Skypro")
                              ]

starts_with_pozitive_list = [
                             ("Skypro", "S", True),
                             ("Skypro", "s", True),
                             ("Skypro", "T", False)
                            ]

starts_with_negative_list = [
                             ("Skypro", "", False),
                             ("Skypro", " ", False),
                             ("Skypro", None, False)
                            ]

end_with_pozitive_list = [
                          ("Skypro", "o", True),
                          ("Skypro", "O", True),
                          ("Skypro", "T", False)
                         ]

end_with_negative_list = [
                          ("Skypro", "о", False),  # "о" - Ру раскладка
                          ("Skypro", "", False),
                          ("Skypro", " ", False),
                          ("Skypro", None, False)
                         ]

is_empty_pozitive_list = [
                          ("", True),
                          (" ", True),
                          ("    ", True)
                         ]

is_empty_negative_list = [
                          (None, True)
                         ]

list_to_string_pozitive_list = [
                                (["1", "2", "3"], ", ", "1, 2, 3"),
                                (["S", "k", "y", "p", "r", "o"], "", "Skypro"),
                                (["!", "#", "&"], "-", "!-#-&")
                               ]

list_to_string_negative_list = [
                                ([], ", ", ""),
                                ([ ], "", ""),
                                (None, "-", "-"),
                                (["1", "2", "3"], None, "1, 2, 3")
                               ]


@pytest.mark.parametrize('text, res', capitilize_pozitive_list)
def test_capitilize_positive(text, res):
    assert utils.capitilize(text) == res


@pytest.mark.parametrize("text, res", capitilize_negative_list)
def test_capitilize_negative(text, res):
    assert utils.capitilize(text) == res


@pytest.mark.parametrize("text, res", trim_pozitive_list)
def test_trim_positive(text, res):
    assert utils.trim(text) == res


@pytest.mark.parametrize("text, res", trim_negative_list)
def test_trim_negative(text, res):
    assert utils.trim(text) == res


@pytest.mark.parametrize("string, delim, res", to_list_pozitive_list)
def test_to_list_pozitive(string, delim, res):
    assert utils.to_list(string, delim) == res


@pytest.mark.parametrize("string, delim, res", to_list_negative_list)
def test_to_list_negative(string, delim, res):
    assert utils.to_list(string, delim) == res


@pytest.mark.parametrize("string, simbol, res", contains_pozitive_list)
def test_contains_pozitive(string, simbol, res):
    assert utils.contains(string, simbol) == res


@pytest.mark.parametrize("string, simbol, res", contains_negative_list)
def test_contains_negative(string, simbol, res):
    assert utils.contains(string, simbol) == res


@pytest.mark.parametrize("string, simbol, res", delete_simbol_pozitive_list)
def test_delete_simbol_pozitive(string, simbol, res):
    assert utils.delete_symbol(string, simbol) == res


@pytest.mark.parametrize("string, simbol, res", delete_simbol_negative_list)
def test_delete_simbol_negative(string, simbol, res):
    assert utils.delete_symbol(string, simbol) == res


@pytest.mark.parametrize("string, symbol, res", starts_with_pozitive_list)
def test_starts_with_pozitive(string, symbol, res):
    assert utils.starts_with(string, symbol) == res


@pytest.mark.parametrize("string, symbol, res", starts_with_negative_list)
def test_starts_with_negative(string, symbol, res):
    assert utils.starts_with(string, symbol) == res


@pytest.mark.parametrize("string, symbol, res", end_with_pozitive_list)
def test_end_with_pozitive(string, symbol, res):
    assert utils.end_with(string, symbol) == res


@pytest.mark.parametrize("string, symbol, res", end_with_negative_list)
def test_end_with_negative(string, symbol, res):
    assert utils.end_with(string, symbol) == res


@pytest.mark.parametrize("string, res", is_empty_pozitive_list)
def test_is_empty_pozitive(string, res):
    assert utils.is_empty(string) == res


@pytest.mark.parametrize("string, res", is_empty_negative_list)
def test_is_empty_negative(string, res):
    assert utils.is_empty(string) == res


@pytest.mark.parametrize("lst, joiner, res", list_to_string_pozitive_list)
def test_list_to_string_pozitive(lst, joiner: str, res):
    assert utils.list_to_string(lst, joiner) == res


@pytest.mark.parametrize("lst, joiner, res", list_to_string_negative_list)
def test_list_to_string_negative(lst, joiner: str, res):
    assert utils.list_to_string(lst, joiner) == res
