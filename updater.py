import os
import shutil
import time
import subprocess
import sys

APP_EXE = "app.exe"
NEW_DIR = "new_version"
APP_DIR = os.getcwd()

def wait_for_app():
    print("Waiting for app to close...")
    while True:
        # simple check: try renaming the exe (fails if in use)
        try:
            os.rename(APP_EXE, APP_EXE)
            break
        except OSError:
            time.sleep(0.2)

def replace_files():
    print("Replacing files...")

    for item in os.listdir(NEW_DIR):
        src = os.path.join(NEW_DIR, item)
        dst = os.path.join(APP_DIR, item)

        if os.path.isdir(src):
            if os.path.exists(dst):
                shutil.rmtree(dst)
            shutil.move(src, dst)
        else:
            if os.path.exists(dst):
                os.remove(dst)
            shutil.move(src, dst)

def cleanup():
    print("Cleaning up...")
    if os.path.exists(NEW_DIR):
        shutil.rmtree(NEW_DIR)

def restart_app():
    print("Restarting app...")
    subprocess.Popen([APP_EXE], shell=True)

def main():
    wait_for_app()
    replace_files()
    cleanup()
    restart_app()

if __name__ == "__main__":
    main()