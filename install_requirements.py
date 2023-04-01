import subprocess

def pip_install(package):
    subprocess.check_call(["pip", "install", package])

def install_requirements():
    try:
        with open("requirements.txt") as f:
            for line in f:
                pip_install(line)
                
    except subprocess.CalledProcessError:
        print("Error installing requirements. Some packages may not be available. This maybe because your desktop doesn't have a GUI.")

if __name__ == "__main__":
    install_requirements()