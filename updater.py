import os
import shutil
import subprocess
import customtkinter as ctk

class UpdaterApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Constants
        self.APP_EXE = "app.exe"
        self.NEW_DIR = "new_version"
        self.APP_DIR = os.getcwd()

        # Window UI Setup
        self.title("Updater")
        self.geometry("400x180")
        self.resizable(False, False)
        
        self.label = ctk.CTkLabel(self, text="Waiting for app to close...", font=("Arial", 14))
        self.label.pack(expand=True, pady=(20, 10))

        self.progress = ctk.CTkProgressBar(self, width=300)
        self.progress.set(0)

        # Start the first check
        self.wait_for_app()

    def wait_for_app(self):
        """Checks if the app is closed without freezing the UI."""
        try:
            # If we can rename it, it's not in use
            os.rename(self.APP_EXE, self.APP_EXE)
            # Success! Move to the next step
            self.replace_files()
        except OSError:
            # Still open? Wait 200ms and try again
            self.after(200, self.wait_for_app)

    def replace_files(self):
        self.label.configure(text="Replacing files...")
        
        # Show and start progress bar for the file operations
        self.progress.pack(pady=10)
        self.progress.start()

        # Run the file operations (Small delay to let the UI update text)
        self.after(1000, self._do_file_work)

    def _do_file_work(self):
        # locked in
        if os.path.exists(self.NEW_DIR):
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
        
        self.cleanup()

    def cleanup(self):
        self.label.configure(text="Cleaning up...")
        if os.path.exists(self.NEW_DIR):
            shutil.rmtree(self.NEW_DIR)
        
        # Short delay before the final step
        self.after(1000, self.restart_app)

    def restart_app(self):
        # Hide progress bar and show final text
        self.progress.stop()
        self.progress.pack_forget()
        
        self.label.configure(text="Restarting app...")
        
        # Launch the app
        subprocess.Popen([self.APP_EXE], shell=True)
        
        # Close the updater after 1.5 seconds
        self.after(1500, self.destroy)

if __name__ == "__main__":
    app = UpdaterApp()
    app.mainloop()

