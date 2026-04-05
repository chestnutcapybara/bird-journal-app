import os
import shutil
import time
import subprocess
import customtkinter as ctk

class Updater():
    def __init__(self):
        self.APP_EXE = "app.exe"
        self.NEW_DIR = "new_version"
        self.APP_DIR = os.getcwd()

        self.wait_for_app()
        self.replace_files()
        self.cleanup()
        self.restart_app()
    def wait_for_app(self):
        print("Waiting for app to close...")
        while True:
        # simple check: try renaming the exe (fails if in use)
            try:
                os.rename(self.APP_EXE, self.APP_EXE)
                break
            except OSError:
                time.sleep(0.2)

    def replace_files(self):
        print("Replacing files...")

        for item in os.listdir(self.NEW_DIR):
            src = os.path.join(self.NEW_DIR, item)
            dst = os.path.join(self.APP_DIR, item)

            if os.path.isdir(src):
                if os.path.exists(dst):
                    shutil.rmtree(dst)
                shutil.move(src, dst)
            else:
                if os.path.exists(dst):
                    os.remove(dst)
                shutil.move(src, dst)

    def cleanup(self):
        print("Cleaning up...")
        if os.path.exists(self.NEW_DIR):
            shutil.rmtree(self.NEW_DIR)

    def restart_app(self):
        print("Restarting app...")
        subprocess.Popen([self.APP_EXE], shell=True)
