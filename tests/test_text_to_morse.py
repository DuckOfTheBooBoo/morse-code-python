from src.morse_code import text_to_morse

"""
TODO: 
- Test that the first function can correctly convert a simple text string to a Morse code string.
- Test that the first function can correctly handle strings containing uppercase letters.
- Test that the first function can correctly handle special characters, such as punctuation marks.
- Test that the first function can handle empty strings and return an empty string.
- Test that the first function can handle strings containing non-alphabetic characters (such as numbers or symbols) and return an error message or raise an exception.
- Test that the first function can handle input strings that are very long and return a Morse code string that is also very long.
- Test that the first function can handle strings containing multiple lines or paragraphs and return a Morse code string with proper spacing.
"""

def test_simple_text():

    input_str = "hello world"
    expected_output = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
    
    assert text_to_morse(input_str) == expected_output, f"Error: Expected {expected_output}, but got {text_to_morse(input_str)}"


def test_uppercase_leter():

    input_str = "WOULD YOU RUN"
    expected_output = ".-- --- ..- .-.. -.. / -.-- --- ..- / .-. ..- -."

    assert text_to_morse(input_str) == expected_output, f"Error: Expected {expected_output}, but got {text_to_morse(input_str)}"
