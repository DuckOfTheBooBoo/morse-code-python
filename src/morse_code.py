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
    Takes a string of text and return morse code string.
    """

    if any(ch.isupper() for ch in text):
        text = text.lower()

    morse_code_list = []

    words = text.split(" ")

    for idx, word in enumerate(words):

        for char in word:

            if char in CHAR_TO_MORSE_DICT.keys():
                morse_code_list.append(CHAR_TO_MORSE_DICT[char])
                morse_code_list.append(" ")

        # Word separator
        morse_code_list.append("/ ")
    
    morse_code_str = ''.join(morse_code_list)
    
    return morse_code_str


def morse_to_char(morse_code_str):

    """
    Takes a morse code string and return to string text.
    """

    text = []

    for morse_code in morse_code_str:

        if morse_code in MORSE_TO_CHAR_DICT.keys():
            text.append(MORSE_TO_CHAR_DICT[morse_code])
        
        elif morse_code == "":
            text.append(" ")
    
    return ''.join(text)

def main():
    text = "Arajdian Altaf"

    result = text_to_morse(text)

    print(result)
            

if __name__ == "__main__":
    main()