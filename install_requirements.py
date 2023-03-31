import subprocess

def install_requirements():
    try:
        with open("requirements.txt") as f:
            requirements = f.read().splitlines()
        subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError:
        print("Error installing requirements. Some packages may not be available. This maybe because your desktop doesn't have a GUI.")

if __name__ == "__main__":
    install_requirements()