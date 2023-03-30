class MorseCodeError(Exception):
    """Throws an error if the character is not found in MORSE_TO_CHAR_DICT."""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)