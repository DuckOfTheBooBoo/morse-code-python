from pydub.playback import play
from src.play_morse import play_morse
from rich.console import Console
from rich.prompt import Prompt, Confirm
from src.morse_code import morse_to_text, text_to_morse
from src.morse_code_error import MorseCodeError, MorseCodeNotFound
from os.path import join
from os import getcwd

# Constants
console = Console()

try:
    from tkinter.filedialog import asksaveasfilename
    from _tkinter import TclError
except ModuleNotFoundError:
    console.print("[yellow]tkinter is not installed.[/]") 

def save_file(audio_file):
    
    file = ""

    try:
        file = asksaveasfilename(initialfile="audio.wav", defaultextension=".wav", filetypes=[("Audio File", ".wav")])

    except TclError:
        
        console.print("[yellow]No desktop found. Most likely because you ran it in a terminal.[/]")

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

    except PermissionError as perm_error:
        console.print(f"Error {perm_error}")

    except FileNotFoundError as file_path_error:
        console.print(f"[red]{file_path_error}. Audio will not be saved.[/].")

def input_text_to_morse():
    text = Prompt.ask(prompt="Text")
    audio_file = None

    if text:
        try:
            result = text_to_morse(text)
            console.print(result)

            try:
                audio_file = play_morse(result)
                play(audio_file)

            except OSError as os_error:
                console.print(f"[red]{os_error}[/], [yellow]your device might don't have an audio device output.[/]")

        except MorseCodeNotFound as morse_error:
            console.print("[red]Exception[/]", morse_error)

        else:
            ask_save = Confirm.ask(prompt="Save audio?")
            if ask_save:
                save_file(audio_file)
    
    else:
        console.print("[yellow bold]Empty input.[/]")

def input_morse_to_text():
    morse_code = Prompt.ask(prompt="Morse Code")

    try:
        result = morse_to_text(morse_code)
        console.print(result)
    except MorseCodeError as morse_error:
        console.print("[red]Exception[/]", morse_error)

def main():
    console.print("[green]Python Morse Code Translator[/]")
    console.print("1. [blue]Text To Morse Code[/]\n2. [blue]Morse Code To Text[/]")

    choice = Prompt.ask(prompt= "Answer", choices=["1", "2"])

    if choice == "1":
        input_text_to_morse()
    
    elif choice == "2":
        input_morse_to_text()


if __name__ == "__main__":
    main()
