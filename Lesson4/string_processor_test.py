from string_processor import StringProcessor


import pytest

string_processor = StringProcessor()


@pytest.mark.parametrize('text, result',
                         [
                          ("привет", "Привет."),
                          ("Привет", "Привет."),
                          ("привет.", "Привет."),
                          ("Привет.", "Привет.")
                          ])
def test_processed_positive(text, result):
    res = string_processor.process("привет.")
    assert res == "Привет."


@pytest.mark.parametrize('text, result',
                         [
                          ("", "."),
                          ("    ", "    .")
                         ]
                         )
def test_processed_negative(text, result):
    res = string_processor.process(text)
    assert res == result
