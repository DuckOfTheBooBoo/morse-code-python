from morse_code import morse_to_text, text_to_morse
from time import sleep
from pydub import AudioSegment
from pydub.playback import play
import os

DASH_PATH = os.path.join("..", "raw", "dash.wav")
DOT_PATH = os.path.join("..", "raw", "dot.wav")

DOT = AudioSegment.from_wav(DOT_PATH)
DASH = AudioSegment.from_wav(DASH_PATH)

morse_code_sounds = {
    ".": DOT,
    "-": DASH,
}

def main():
    test = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
    morse_audio = AudioSegment.empty()

    for char in test:
        if char in morse_code_sounds:
            sound = morse_code_sounds[char]
            morse_audio += sound
            
    play(morse_audio)

if __name__ == "__main__":
    main()