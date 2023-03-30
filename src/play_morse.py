from morse_code import morse_to_text, text_to_morse
from time import sleep
from pydub import AudioSegment
from pydub.playback import play
import os

DASH_PATH = os.path.join("..", "raw", "dash.wav")
DOT_PATH = os.path.join("..", "raw", "dot.wav")
CHAR_SPACE_PATH = os.path.join("..", "raw", "char_space.wav")
WORD_SPACE_PATH = os.path.join("..", "raw", "word_space.wav")

DOT = AudioSegment.from_wav(DOT_PATH)
DASH = AudioSegment.from_wav(DASH_PATH)
CHAR_SPACE = AudioSegment.from_wav(CHAR_SPACE_PATH)
WORD_SPACE = AudioSegment.from_wav(WORD_SPACE_PATH)

morse_code_sounds = {
    ".": DOT,
    "-": DASH,
    " ": CHAR_SPACE,
    " / ": WORD_SPACE
}

def main():
    test = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
    morse_audio = AudioSegment.empty()

    test_mod = test.split(" / ")

    for sequence in test:
        for code in sequence:
            if code in morse_code_sounds:
                sound = morse_code_sounds[code]
                # morse_audio += sound
                play(sound)
            
    # play(morse_audio)

if __name__ == "__main__":
    main()