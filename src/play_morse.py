from morse_code import morse_to_text, text_to_morse
from time import sleep
from pydub import AudioSegment
from pydub.playback import play
from pydub.generators import Sine
import os

DOT = Sine(500).to_audio_segment(duration=50)
DASH = Sine(500).to_audio_segment(duration=150)
INTRA_CHAR_SPACE = AudioSegment.silent(duration=50)
INTER_CHAR_SPACE = AudioSegment.silent(duration=150)
WORD_SPACE = AudioSegment.silent(duration=350)

def play_morse():
    test = "-.- --.."
    morse_audio = AudioSegment.empty()

    audio_segment_visual = []

    if " / " in test:
        sequences = test.split(" / ")
    else:
        sequences = [test,]

    for word_index, word in enumerate(sequences):
        letters = word.split(" ")

        for char_index, char in enumerate(letters):
            for symbol_index, symbol in enumerate(char):
                
                if symbol == ".":
                    morse_audio += DOT
                    audio_segment_visual.append("DOT")
                elif symbol == "-":
                    morse_audio += DASH
                    audio_segment_visual.append("DASH")
                
                if symbol_index != len(char) - 1:
                    # Add silence between characters
                    morse_audio += INTRA_CHAR_SPACE
                    audio_segment_visual.append("INTRA_CHAR_SPACE")
                else:
                    # Add silence between letters
                    morse_audio += INTER_CHAR_SPACE
                    audio_segment_visual.append("INTER_CHAR_SPACE")
        
        if word_index == len(sequences) - 1:
            # Add silence between words
            morse_audio += WORD_SPACE   
            audio_segment_visual.append("WORD_SPACE")
            
    # play(morse_audio)
    return audio_segment_visual

if __name__ == "__main__":
    play_morse()