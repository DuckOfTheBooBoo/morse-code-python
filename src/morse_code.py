from time import sleep

MORSE_TO_CHAR_DICT = {
    '.-': 'a',
    '-...': 'b',
    '-.-.': 'c',
    '-..': 'd',
    '.': 'e',
    '..-.': 'f',
    '--.': 'g',
    '....': 'h',
    '..': 'i',
    '.---': 'j',
    '-.-': 'k',
    '.-..': 'l',
    '--': 'm',
    '-.': 'n',
    '---': 'o',
    '.--.': 'p',
    '--.-': 'q',
    '.-.': 'r',
    '...': 's',
    '-': 't',
    '..-': 'u',
    '...-': 'v',
    '.--': 'w',
    '-..-': 'x',
    '-.--': 'y',
    '--..': 'z',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '-----': '0'
}
CHAR_TO_MORSE_DICT = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----'
}

def text_to_morse(text):

    """
    Takes a string of text and return a morse code string.
    """

    if any(ch.isupper() for ch in text):
        text = text.lower()

    morse_code_list = []

    words = text.split(" ")

    for word_index, word in enumerate(words):
        for char_index, char in enumerate(word):

            if char in CHAR_TO_MORSE_DICT.keys():
                morse_code_list.append(CHAR_TO_MORSE_DICT[char])
                morse_code_list.append(" ")

            if char_index == len(word) - 1 and word_index != len(words) - 1:
                morse_code_list.append("/ ")

    # Remove trailing whitespace
    morse_code_list.pop()

    morse_code_str = ''.join(morse_code_list)

    return morse_code_str

def morse_to_text(morse_code_str):

    """
    Takes a morse code string and return to string text.
    """

    text = []

    morse_words = morse_code_str.split("/ ")


    for idx, morse_word in enumerate(morse_words):

        morse_letter = morse_word.split(" ")

        for morse_code in morse_letter:

            if morse_code in MORSE_TO_CHAR_DICT.keys():
                text.append(MORSE_TO_CHAR_DICT[morse_code])
        
        if idx != len(morse_words) - 1:
            text.append(" ")
        
    return ''.join(text)

def main():
    text = "hello world"
    morse = text_to_morse(text)
    # new_text = morse_to_text(morse)

    with open("out.txt", "w") as file:
        file.writelines(morse)

if __name__ == "__main__":
    main()