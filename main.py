from rich.console import Console
from rich.prompt import Prompt, Confirm
from src.morse_code import morse_to_text, text_to_morse
from src.play_morse import play_morse
from src.morse_code_error import MorseCodeError, MorseCodeNotFound

console = Console()

def main():
    console.print("[green]Python Morse Code Translator[/]")
    console.print("1. [blue]Text To Morse Code[/]\n2. [blue]Morse Code To Text[/]")

    choice = Prompt.ask(prompt= "Answer", choices=["1", "2"])

    if choice == "1":
        text = Prompt.ask(prompt="Text")

        try:
            result = text_to_morse(text)
            console.print(result)
            play_morse(result)
        except MorseCodeNotFound as e:
            console.print("[red]Exception[/]", e)
    
    elif choice == "2":
        morse_code = Prompt.ask(prompt="Morse Code")

        try:
            result = morse_to_text(morse_code)
            console.print(result)
        except MorseCodeError as e:
            console.print("[red]Exception[/]", e)


if __name__ == "__main__":
    main()