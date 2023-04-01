from rich.console import Console
import subprocess

console = Console()
def pip_install(package):
    subprocess.check_call(["pip", "install", package])

def install_requirements():
    try:
        with open("requirements.txt") as f:
            for line in f:
                pip_install(line)
                
    except subprocess.CalledProcessError:
        console.print("Error installing requirements. Your device might missing portaudio and pyaudio.\nTry installing them with\n[bold white]sudo apt install portaudio19-dev python3-pyaudio[/]")



if __name__ == "__main__":
    install_requirements()