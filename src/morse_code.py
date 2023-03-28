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

def char_to_morse(text):

    if any(ch.isupper() for ch in text):
        text = text.lower()

    morse_code_list = []

    for char in text:
        
        if char in CHAR_TO_MORSE.keys():
            morse_code.append(CHAR_TO_MORSE[char])
            morse_code.append(" ")

        elif char == " ":
            morse_code.append(" ")
    
    morse_code_str = ''.join(morse_code)
    
    return morse_code_str


def morse_to_char(morse_code_str):
    text = []

    for morse_code in morse_code_str:

        if morse_code in MORSE_TO_CHAR.keys():
            text.append(MORSE_TO_CHAR[m_code])
        
        elif morse_code == "":
            text.append(" ")
    
    return ''.join(text)

def main():
    pass
            

if __name__ == "__main__":
    main()