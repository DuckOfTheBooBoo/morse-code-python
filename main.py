from tkinter.filedialog import asksaveasfilename
from _tkinter import TclError
from rich.console import Console
from rich.prompt import Prompt, Confirm
from src.morse_code import morse_to_text, text_to_morse
from src.morse_code_error import MorseCodeError, MorseCodeNotFound
from os.path import join
from os import getcwd

# Constants
console = Console()
PYAUDIO_EXIST = None

try:
    import pyaudio
except ModuleNotFoundError:
    console.print("[yellow]PyAudio is not installed. Morse code cannot be played.[/]")
    PYAUDIO_EXIST = False

else:
    PYAUDIO_EXIST = True
    from pydub.playback import play
    from src.play_morse import play_morse


def main():
    console.print("[green]Python Morse Code Translator[/]")
    console.print("1. [blue]Text To Morse Code[/]\n2. [blue]Morse Code To Text[/]")

    choice = Prompt.ask(prompt= "Answer", choices=["1", "2"])

    if choice == "1":
        text = Prompt.ask(prompt="Text")
        audio_file = None

        try:
            result = text_to_morse(text)
            console.print(result)

            if PYAUDIO_EXIST:
                audio_file = play_morse(result)
                play(audio_file)

        except MorseCodeNotFound as e:
            console.print("[red]Exception[/]", e)

        else:
            ask_save = Confirm.ask(prompt="Save audio?")

            if ask_save:
                
                file = ""

                try:
                    file = asksaveasfilename(initialfile="audio.wav", defaultextension=".wav", filetypes=[("Audio File", ".wav")])

                except TclError:
                    
                    console.print("[yellow]No desktop found. This most likely because you ran it in a terminal.[/]")

                    while True:
                        input_filename = Prompt.ask(prompt="File path: ", default="audio.wav")

                        if not input_filename.endswith(".wav"):
                            input_filename += ".wav"

                        current_path = getcwd()

                        console.log(join(current_path, input_filename))

                        file_path_confirm = Confirm.ask("Correct?")

                        if file_path_confirm:
                            file = join(current_path, input_filename)
                            break
                        else:
                            pass
                
                try:
                    audio_file.export(file, format="wav")
                except PermissionError as e:
                    console.print(f"Error {e}")

            else:
                pass

    elif choice == "2":
        morse_code = Prompt.ask(prompt="Morse Code")

        try:
            result = morse_to_text(morse_code)
            console.print(result)
        except MorseCodeError as e:
            console.print("[red]Exception[/]", e)


if __name__ == "__main__":
    main()