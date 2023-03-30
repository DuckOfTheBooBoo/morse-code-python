import pytest
from python_morse_code.src.play_morse import play_morse

DASH = "DASH"
DOT = "DOT"
INTRASPACE = "INTRA_CHAR_SPACE"
INTERSPACE = "INTER_CHAR_SPACE"
WORDSPACE = "WORD_SPACE"

def test_one_word():

    input_str = ".... . .-.. .-.. ---"
    expected_output = [DOT, INTRASPACE, DOT, INTRASPACE, DOT, INTRASPACE, DOT, INTERSPACE, DOT, INTERSPACE, DOT, INTRASPACE, DASH, INTRASPACE, DOT, INTRASPACE, DOT, INTERSPACE, DASH, INTRASPACE, DASH, INTRASPACE, DASH, INTERSPACE, DASH]

    assert play_morse(input_str) == expected_output, f"Error: Expected {expected_output}, but got {morse_to_text(input_str)}"