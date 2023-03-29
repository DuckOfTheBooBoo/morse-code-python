from src.morse_code import text_to_morse, morse_to_text
import pytest

"""
TODO:
- Test that the second function can correctly convert a simple Morse code string to a text string.
- Test that the second function can correctly handle Morse code strings containing multiple spaces between characters.
- Test that the second function can correctly handle Morse code strings containing special characters.
- Test that the second function can handle empty Morse code strings and return an empty string.
- Test that the second function can handle Morse code strings containing invalid Morse code characters and return an error message or raise an exception.
- Test that the second function can handle Morse code strings containing invalid Morse code sequences and return an error message or raise an exception.
- Test that the second function can handle very long Morse code strings and return a text string that is also very long.
- Test that the second function can handle Morse code strings containing multiple lines or paragraphs and return a text string with proper spacing.
"""

def test_simple_morse_to_string():

    input_str = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
    expected_output = "HELLO WORLD"

    assert morse_to_text(input_str) == expected_output, f"Error: Expected {expected_output}, but got {morse_to_text(input_str)}"

def test_multiple_spaces():

    input_str = ".... . .-..   .-..  --- / .--  ---   .-. .-.. -.."
    expected_output = "HELLO WORLD"

    assert morse_to_text(input_str) == expected_output, f"Error: Expected {expected_output}, but got {morse_to_text(input_str)}"

def test_special_char():

    input_str = "- .... .. ... / ... . -. - . -. -.-. . / -.-. --- -. - .- .. -. ... / .--. ..- -. -.-. - ..- .- - .. --- -. / .-... / ... .--. . -.-. .. .- .-.. / -.-. .... .- .-. .- -.-. - . .-. ... -.-.--"
    expected_output = "THIS SENTENCE CONTAINS PUNCTUATION & SPECIAL CHARACTERS!"

    assert morse_to_text(input_str) == expected_output, f"Error: Expected {expected_output}, but got {morse_to_text(input_str)}"

def test_empty_morse():

    input_str = ""
    expected_output = ""

    assert morse_to_text(input_str) == expected_output, f"Error: Expected {expected_output}, but got {morse_to_text(input_str)}"


def test_invalid_morse_code():

    input_str = "... --- ... $"
    expected_output = "INVALID MORSE CODE"

    with pytest.raises(ValueError):
        morse_to_text(input_str)

def test_long_morse_code():

    input_str = ".-- .... .. .-.. . / .--. -.-- - .... --- -. / .. ... / .- / .-- .. -.. . .-.. -.-- / ..- ... . -.. / .--. .-. --- --. .-. .- -- -- .. -. --. / .-.. .- -. --. ..- .- --. . / .-- .. - .... / -- .- -. -.-- / .- -.. ...- .- -. - .- --. . ... --..-- / .. - / .- .-.. ... --- / .... .- ... / ... --- -- . / -.. .-. .- .-- -... .- -.-. -.- ... / - .... .- - / -.. . ...- . .-.. --- .--. . .-. ... / ... .... --- ..- .-.. -.. / -... . / .- .-- .- .-. . / --- ..-. .-.-.- / --- -. . / --- ..-. / - .... . / -- .- .. -. / -.-. --- -. ... / --- ..-. / .--. -.-- - .... --- -. / .. ... / .. - ... / .--. . .-. ..-. --- .-. -- .- -. -.-. . / -.-. --- -- .--. .- .-. . -.. / - --- / .-.. --- .-- . .-. -....- .-.. . ...- . .-.. / .-.. .- -. --. ..- .- --. . ... / .-.. .. -.- . / -.-. / --- .-. / -.-. .-.-. .-.-. .-.-.- / ... .. -. -.-. . / .--. -.-- - .... --- -. / .. ... / .- -. / .. -. - . .-. .--. .-. . - . -.. / .-.. .- -. --. ..- .- --. . --..-- / .. - / -.-. .- -. / -... . / ... .-.. --- .-- . .-. / - .... .- -. / -.-. --- -- .--. .. .-.. . -.. / .-.. .- -. --. ..- .- --. . ... --..-- / .--. .- .-. - .. -.-. ..- .-.. .- .-. .-.. -.-- / .-- .... . -. / .-- --- .-. -.- .. -. --. / .-- .. - .... / .-.. .- .-. --. . / -.. .- - .- ... . - ... / --- .-. / .--. . .-. ..-. --- .-. -- .. -. --. / -.-. --- -- .--. .-.. . -..- / -.-. --- -- .--. ..- - .- - .. --- -. ... .-.-.- / .- -.. -.. .. - .. --- -. .- .-.. .-.. -.-- --..-- / .--. -.-- - .... --- -. .----. ... / -.. -.-- -. .- -- .. -.-. .- .-.. .-.. -.-- -....- - -.-- .--. . -.. / -. .- - ..- .-. . / -.-. .- -. / .-.. . .- -.. / - --- / ..- -. . -..- .--. . -.-. - . -.. / . .-. .-. --- .-. ... / .- -. -.. / -... ..- --. ... / - .... .- - / -.-. .- -. / -... . / -.. .. ..-. ..-. .. -.-. ..- .-.. - / - --- / -.. . -... ..- --. .-.-.- / .- -. --- - .... . .-. / .--. --- - . -. - .. .- .-.. / .. ... ... ..- . / .-- .. - .... / .--. -.-- - .... --- -. / .. ... / ...- . .-. ... .. --- -. / -.-. --- -- .--. .- - .. -... .. .-.. .. - -.-- --..-- / .- ... / -.. .. ..-. ..-. . .-. . -. - / ...- . .-. ... .. --- -. ... / --- ..-. / .--. -.-- - .... --- -. / -- .- -.-- / .... .- ...- . / -.. .. ..-. ..-. . .-. . -. - / ... -.-- -. - .- -..- / .- -. -.. / .-.. .. -... .-. .- .-. -.-- / ... ..- .--. .--. --- .-. - --..-- / -- .- -.- .. -. --. / .. - / -.-. .... .- .-.. .-.. . -. --. .. -. --. / - --- / -- .- .. -. - .- .. -. / -.-. --- -.. . / .- -.-. .-. --- ... ... / -.. .. ..-. ..-. . .-. . -. - / . -. ...- .. .-. --- -. -- . -. - ... .-.-.- / ..-. .. -. .- .-.. .-.. -.-- --..-- / .-- .... .. .-.. . / .--. -.-- - .... --- -. / .... .- ... / .- -. / . -..- - . -. ... .. ...- . / .-.. .. -... .-. .- .-. -.-- / --- ..-. / -- --- -.. ..- .-.. . ... / .- -. -.. / - --- --- .-.. ... --..-- / .. - / -- .- -.-- / -. --- - / -... . / - .... . / -... . ... - / -.-. .... --- .. -.-. . / ..-. --- .-. / -.-. . .-. - .- .. -. / .- .--. .--. .-.. .. -.-. .- - .. --- -. ... / - .... .- - / .-. . --.- ..- .. .-. . / ... .--. . -.-. .. ..-. .. -.-. / -. .. -.-. .... . / - . -.-. .... -. --- .-.. --- --. .. . ... / --- .-. / .-. . --.- ..- .. .-. . / -- .- -..- .. -- ..- -- / .--. . .-. ..-. --- .-. -- .- -. -.-. . .-.-.- / -.. . ... .--. .. - . / - .... . ... . / -.-. --- -. ... --..-- / .--. -.-- - .... --- -. / .-. . -- .- .. -. ... / .- / .--. --- .--. ..- .-.. .- .-. / -.-. .... --- .. -.-. . / .- -- --- -. --. / -.. . ...- . .-.. --- .--. . .-. ... / -.. ..- . / - --- / .. - ... / ... .. -- .--. .-.. .. -.-. .. - -.-- --..-- / ...- . .-. ... .- - .. .-.. .. - -.-- --..-- / .- -. -.. / -... .-. --- .- -.. / .-. .- -. --. . / --- ..-. / .- .--. .--. .-.. .. -.-. .- - .. --- -. ... .-.-.-"
    expected_output = "WHILE PYTHON IS A WIDELY USED PROGRAMMING LANGUAGE WITH MANY ADVANTAGES, IT ALSO HAS SOME DRAWBACKS THAT DEVELOPERS SHOULD BE AWARE OF. ONE OF THE MAIN CONS OF PYTHON IS ITS PERFORMANCE COMPARED TO LOWER-LEVEL LANGUAGES LIKE C OR C++. SINCE PYTHON IS AN INTERPRETED LANGUAGE, IT CAN BE SLOWER THAN COMPILED LANGUAGES, PARTICULARLY WHEN WORKING WITH LARGE DATASETS OR PERFORMING COMPLEX COMPUTATIONS. ADDITIONALLY, PYTHON'S DYNAMICALLY-TYPED NATURE CAN LEAD TO UNEXPECTED ERRORS AND BUGS THAT CAN BE DIFFICULT TO DEBUG. ANOTHER POTENTIAL ISSUE WITH PYTHON IS VERSION COMPATIBILITY, AS DIFFERENT VERSIONS OF PYTHON MAY HAVE DIFFERENT SYNTAX AND LIBRARY SUPPORT, MAKING IT CHALLENGING TO MAINTAIN CODE ACROSS DIFFERENT ENVIRONMENTS. FINALLY, WHILE PYTHON HAS AN EXTENSIVE LIBRARY OF MODULES AND TOOLS, IT MAY NOT BE THE BEST CHOICE FOR CERTAIN APPLICATIONS THAT REQUIRE SPECIFIC NICHE TECHNOLOGIES OR REQUIRE MAXIMUM PERFORMANCE. DESPITE THESE CONS, PYTHON REMAINS A POPULAR CHOICE AMONG DEVELOPERS DUE TO ITS SIMPLICITY, VERSATILITY, AND BROAD RANGE OF APPLICATIONS."

    assert morse_to_text(input_str) == expected_output, f"Error: Expected {expected_output}, but got {morse_to_text(input_str)}"
