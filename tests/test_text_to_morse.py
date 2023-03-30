import pytest
from src.morse_code import text_to_morse

def test_simple_text():

    input_str = "hello world"
    expected_output = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
    
    assert text_to_morse(input_str) == expected_output, f"Error: Expected {expected_output}, but got {text_to_morse(input_str)}"


def test_uppercase_leter():

    input_str = "WOULD YOU RUN"
    expected_output = ".-- --- ..- .-.. -.. / -.-- --- ..- / .-. ..- -."

    assert text_to_morse(input_str) == expected_output, f"Error: Expected {expected_output}, but got {text_to_morse(input_str)}"

def test_punctuation_marks():

    input_str = "Hello, World! How are you?"
    expected_output = ".... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.-- / .... --- .-- / .- .-. . / -.-- --- ..- ..--.."

    assert text_to_morse(input_str) == expected_output, f"Error: Expected {expected_output}, but got {text_to_morse(input_str)}"

def test_empty_string():

    input_str = ""
    expected_output = ""

    assert text_to_morse(input_str) == expected_output, f"Error: Expected {expected_output}, but got {text_to_morse(input_str)}"

def test_long_string():

    input_str = "It's important to note that each test function should ideally test a single behavior or feature. This allows you to isolate failures and pinpoint issues more easily. However, it's perfectly acceptable to have multiple assertions within a single test function as long as they're all testing the same behavior or feature."

    expected_output = ".. - .----. ... / .. -- .--. --- .-. - .- -. - / - --- / -. --- - . / - .... .- - / . .- -.-. .... / - . ... - / ..-. ..- -. -.-. - .. --- -. / ... .... --- ..- .-.. -.. / .. -.. . .- .-.. .-.. -.-- / - . ... - / .- / ... .. -. --. .-.. . / -... . .... .- ...- .. --- .-. / --- .-. / ..-. . .- - ..- .-. . .-.-.- / - .... .. ... / .- .-.. .-.. --- .-- ... / -.-- --- ..- / - --- / .. ... --- .-.. .- - . / ..-. .- .. .-.. ..- .-. . ... / .- -. -.. / .--. .. -. .--. --- .. -. - / .. ... ... ..- . ... / -- --- .-. . / . .- ... .. .-.. -.-- .-.-.- / .... --- .-- . ...- . .-. --..-- / .. - .----. ... / .--. . .-. ..-. . -.-. - .-.. -.-- / .- -.-. -.-. . .--. - .- -... .-.. . / - --- / .... .- ...- . / -- ..- .-.. - .. .--. .-.. . / .- ... ... . .-. - .. --- -. ... / .-- .. - .... .. -. / .- / ... .. -. --. .-.. . / - . ... - / ..-. ..- -. -.-. - .. --- -. / .- ... / .-.. --- -. --. / .- ... / - .... . -.-- .----. .-. . / .- .-.. .-.. / - . ... - .. -. --. / - .... . / ... .- -- . / -... . .... .- ...- .. --- .-. / --- .-. / ..-. . .- - ..- .-. . .-.-.-"

    assert text_to_morse(input_str) == expected_output, f"Error: Expected {expected_output}, but got {text_to_morse(input_str)}"

def test_multiple_line_string():
    
    input_str = """Python is a popular programming language that is widely used for various purposes such as web development, data analysis, artificial intelligence, and more. It is known for its simplicity, readability, and easy-to-learn syntax, making it a popular choice among beginners and experienced developers alike. While Python is a widely used programming language with many advantages, it also has some drawbacks that developers should be aware of. One of the main cons of Python is its performance compared to lower-level languages like C or C++. Since Python is an interpreted language, it can be slower than compiled languages, particularly when working with large datasets or performing complex computations."""

    expected_output = ".--. -.-- - .... --- -. / .. ... / .- / .--. --- .--. ..- .-.. .- .-. / .--. .-. --- --. .-. .- -- -- .. -. --. / .-.. .- -. --. ..- .- --. . / - .... .- - / .. ... / .-- .. -.. . .-.. -.-- / ..- ... . -.. / ..-. --- .-. / ...- .- .-. .. --- ..- ... / .--. ..- .-. .--. --- ... . ... / ... ..- -.-. .... / .- ... / .-- . -... / -.. . ...- . .-.. --- .--. -- . -. - --..-- / -.. .- - .- / .- -. .- .-.. -.-- ... .. ... --..-- / .- .-. - .. ..-. .. -.-. .. .- .-.. / .. -. - . .-.. .-.. .. --. . -. -.-. . --..-- / .- -. -.. / -- --- .-. . .-.-.- / .. - / .. ... / -.- -. --- .-- -. / ..-. --- .-. / .. - ... / ... .. -- .--. .-.. .. -.-. .. - -.-- --..-- / .-. . .- -.. .- -... .. .-.. .. - -.-- --..-- / .- -. -.. / . .- ... -.-- -....- - --- -....- .-.. . .- .-. -. / ... -.-- -. - .- -..- --..-- / -- .- -.- .. -. --. / .. - / .- / .--. --- .--. ..- .-.. .- .-. / -.-. .... --- .. -.-. . / .- -- --- -. --. / -... . --. .. -. -. . .-. ... / .- -. -.. / . -..- .--. . .-. .. . -. -.-. . -.. / -.. . ...- . .-.. --- .--. . .-. ... / .- .-.. .. -.- . .-.-.- / .-- .... .. .-.. . / .--. -.-- - .... --- -. / .. ... / .- / .-- .. -.. . .-.. -.-- / ..- ... . -.. / .--. .-. --- --. .-. .- -- -- .. -. --. / .-.. .- -. --. ..- .- --. . / .-- .. - .... / -- .- -. -.-- / .- -.. ...- .- -. - .- --. . ... --..-- / .. - / .- .-.. ... --- / .... .- ... / ... --- -- . / -.. .-. .- .-- -... .- -.-. -.- ... / - .... .- - / -.. . ...- . .-.. --- .--. . .-. ... / ... .... --- ..- .-.. -.. / -... . / .- .-- .- .-. . / --- ..-. .-.-.- / --- -. . / --- ..-. / - .... . / -- .- .. -. / -.-. --- -. ... / --- ..-. / .--. -.-- - .... --- -. / .. ... / .. - ... / .--. . .-. ..-. --- .-. -- .- -. -.-. . / -.-. --- -- .--. .- .-. . -.. / - --- / .-.. --- .-- . .-. -....- .-.. . ...- . .-.. / .-.. .- -. --. ..- .- --. . ... / .-.. .. -.- . / -.-. / --- .-. / -.-. .-.-. .-.-. .-.-.- / ... .. -. -.-. . / .--. -.-- - .... --- -. / .. ... / .- -. / .. -. - . .-. .--. .-. . - . -.. / .-.. .- -. --. ..- .- --. . --..-- / .. - / -.-. .- -. / -... . / ... .-.. --- .-- . .-. / - .... .- -. / -.-. --- -- .--. .. .-.. . -.. / .-.. .- -. --. ..- .- --. . ... --..-- / .--. .- .-. - .. -.-. ..- .-.. .- .-. .-.. -.-- / .-- .... . -. / .-- --- .-. -.- .. -. --. / .-- .. - .... / .-.. .- .-. --. . / -.. .- - .- ... . - ... / --- .-. / .--. . .-. ..-. --- .-. -- .. -. --. / -.-. --- -- .--. .-.. . -..- / -.-. --- -- .--. ..- - .- - .. --- -. ... .-.-.-"

    assert text_to_morse(input_str) == expected_output, f"Error: Expected {expected_output}, but got {text_to_morse(input_str)}"
