# install for local setup with vscode
import subprocess
import os

# validated for python 3.12.2
def install_packages():
    """Define the command to create a virtual environment"""
    if os.name == 'nt':
        print('creating environment windows')
        subprocess.call(r"py -m venv .venv", shell=True)
        venv_activate_cmd = r".venv\Scripts\activate && "
    else:  # macOS/Linux
        print('creating environment linux or macos')
        subprocess.call(r"python3.12 -m venv .venv", shell=True)
        venv_activate_cmd = r"source .venv/bin/activate && "

    print("Install Dependencies...")
    subprocess.call(venv_activate_cmd + r"pip install uv==0.4.7", shell=True)
    install_cmd = "uv pip install -e ."
    result = subprocess.call(venv_activate_cmd + install_cmd, shell=True)
    if result==0:
        print("\n\n----Installation Complete!----")
    else:
        raise RuntimeError("\n\n----Failure During Installation!----")
    
if __name__ == "__main__":
    install_packages()