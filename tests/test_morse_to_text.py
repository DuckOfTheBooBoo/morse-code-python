import pytest
from src.morse_code import morse_to_text
from src.morse_code_error import MorseCodeError

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

    with pytest.raises(MorseCodeError, match=expected_output):
        morse_to_text(input_str)

def test_long_morse_code():

    input_str = ".-- .... .. .-.. . / .--. -.-- - .... --- -. / .. ... / .- / .-- .. -.. . .-.. -.-- / ..- ... . -.. / .--. .-. --- --. .-. .- -- -- .. -. --. / .-.. .- -. --. ..- .- --. . / .-- .. - .... / -- .- -. -.-- / .- -.. ...- .- -. - .- --. . ... --..-- / .. - / .- .-.. ... --- / .... .- ... / ... --- -- . / -.. .-. .- .-- -... .- -.-. -.- ... / - .... .- - / -.. . ...- . .-.. --- .--. . .-. ... / ... .... --- ..- .-.. -.. / -... . / .- .-- .- .-. . / --- ..-. .-.-.- / --- -. . / --- ..-. / - .... . / -- .- .. -. / -.-. --- -. ... / --- ..-. / .--. -.-- - .... --- -. / .. ... / .. - ... / .--. . .-. ..-. --- .-. -- .- -. -.-. . / -.-. --- -- .--. .- .-. . -.. / - --- / .-.. --- .-- . .-. -....- .-.. . ...- . .-.. / .-.. .- -. --. ..- .- --. . ... / .-.. .. -.- . / -.-. / --- .-. / -.-. .-.-. .-.-. .-.-.- / ... .. -. -.-. . / .--. -.-- - .... --- -. / .. ... / .- -. / .. -. - . .-. .--. .-. . - . -.. / .-.. .- -. --. ..- .- --. . --..-- / .. - / -.-. .- -. / -... . / ... .-.. --- .-- . .-. / - .... .- -. / -.-. --- -- .--. .. .-.. . -.. / .-.. .- -. --. ..- .- --. . ... --..-- / .--. .- .-. - .. -.-. ..- .-.. .- .-. .-.. -.-- / .-- .... . -. / .-- --- .-. -.- .. -. --. / .-- .. - .... / .-.. .- .-. --. . / -.. .- - .- ... . - ... / --- .-. / .--. . .-. ..-. --- .-. -- .. -. --. / -.-. --- -- .--. .-.. . -..- / -.-. --- -- .--. ..- - .- - .. --- -. ... .-.-.- / .- -.. -.. .. - .. --- -. .- .-.. .-.. -.-- --..-- / .--. -.-- - .... --- -. .----. ... / -.. -.-- -. .- -- .. -.-. .- .-.. .-.. -.-- -....- - -.-- .--. . -.. / -. .- - ..- .-. . / -.-. .- -. / .-.. . .- -.. / - --- / ..- -. . -..- .--. . -.-. - . -.. / . .-. .-. --- .-. ... / .- -. -.. / -... ..- --. ... / - .... .- - / -.-. .- -. / -... . / -.. .. ..-. ..-. .. -.-. ..- .-.. - / - --- / -.. . -... ..- --. .-.-.- / .- -. --- - .... . .-. / .--. --- - . -. - .. .- .-.. / .. ... ... ..- . / .-- .. - .... / .--. -.-- - .... --- -. / .. ... / ...- . .-. ... .. --- -. / -.-. --- -- .--. .- - .. -... .. .-.. .. - -.-- --..-- / .- ... / -.. .. ..-. ..-. . .-. . -. - / ...- . .-. ... .. --- -. ... / --- ..-. / .--. -.-- - .... --- -. / -- .- -.-- / .... .- ...- . / -.. .. ..-. ..-. . .-. . -. - / ... -.-- -. - .- -..- / .- -. -.. / .-.. .. -... .-. .- .-. -.-- / ... ..- .--. .--. --- .-. - --..-- / -- .- -.- .. -. --. / .. - / -.-. .... .- .-.. .-.. . -. --. .. -. --. / - --- / -- .- .. -. - .- .. -. / -.-. --- -.. . / .- -.-. .-. --- ... ... / -.. .. ..-. ..-. . .-. . -. - / . -. ...- .. .-. --- -. -- . -. - ... .-.-.- / ..-. .. -. .- .-.. .-.. -.-- --..-- / .-- .... .. .-.. . / .--. -.-- - .... --- -. / .... .- ... / .- -. / . -..- - . -. ... .. ...- . / .-.. .. -... .-. .- .-. -.-- / --- ..-. / -- --- -.. ..- .-.. . ... / .- -. -.. / - --- --- .-.. ... --..-- / .. - / -- .- -.-- / -. --- - / -... . / - .... . / -... . ... - / -.-. .... --- .. -.-. . / ..-. --- .-. / -.-. . .-. - .- .. -. / .- .--. .--. .-.. .. -.-. .- - .. --- -. ... / - .... .- - / .-. . --.- ..- .. .-. . / ... .--. . -.-. .. ..-. .. -.-. / -. .. -.-. .... . / - . -.-. .... -. --- .-.. --- --. .. . ... / --- .-. / .-. . --.- ..- .. .-. . / -- .- -..- .. -- ..- -- / .--. . .-. ..-. --- .-. -- .- -. -.-. . .-.-.- / -.. . ... .--. .. - . / - .... . ... . / -.-. --- -. ... --..-- / .--. -.-- - .... --- -. / .-. . -- .- .. -. ... / .- / .--. --- .--. ..- .-.. .- .-. / -.-. .... --- .. -.-. . / .- -- --- -. --. / -.. . ...- . .-.. --- .--. . .-. ... / -.. ..- . / - --- / .. - ... / ... .. -- .--. .-.. .. -.-. .. - -.-- --..-- / ...- . .-. ... .- - .. .-.. .. - -.-- --..-- / .- -. -.. / -... .-. --- .- -.. / .-. .- -. --. . / --- ..-. / .- .--. .--. .-.. .. -.-. .- - .. --- -. ... .-.-.-"
    expected_output = "WHILE PYTHON IS A WIDELY USED PROGRAMMING LANGUAGE WITH MANY ADVANTAGES, IT ALSO HAS SOME DRAWBACKS THAT DEVELOPERS SHOULD BE AWARE OF. ONE OF THE MAIN CONS OF PYTHON IS ITS PERFORMANCE COMPARED TO LOWER-LEVEL LANGUAGES LIKE C OR C++. SINCE PYTHON IS AN INTERPRETED LANGUAGE, IT CAN BE SLOWER THAN COMPILED LANGUAGES, PARTICULARLY WHEN WORKING WITH LARGE DATASETS OR PERFORMING COMPLEX COMPUTATIONS. ADDITIONALLY, PYTHON'S DYNAMICALLY-TYPED NATURE CAN LEAD TO UNEXPECTED ERRORS AND BUGS THAT CAN BE DIFFICULT TO DEBUG. ANOTHER POTENTIAL ISSUE WITH PYTHON IS VERSION COMPATIBILITY, AS DIFFERENT VERSIONS OF PYTHON MAY HAVE DIFFERENT SYNTAX AND LIBRARY SUPPORT, MAKING IT CHALLENGING TO MAINTAIN CODE ACROSS DIFFERENT ENVIRONMENTS. FINALLY, WHILE PYTHON HAS AN EXTENSIVE LIBRARY OF MODULES AND TOOLS, IT MAY NOT BE THE BEST CHOICE FOR CERTAIN APPLICATIONS THAT REQUIRE SPECIFIC NICHE TECHNOLOGIES OR REQUIRE MAXIMUM PERFORMANCE. DESPITE THESE CONS, PYTHON REMAINS A POPULAR CHOICE AMONG DEVELOPERS DUE TO ITS SIMPLICITY, VERSATILITY, AND BROAD RANGE OF APPLICATIONS."

    assert morse_to_text(input_str) == expected_output, f"Error: Expected {expected_output}, but got {morse_to_text(input_str)}"
