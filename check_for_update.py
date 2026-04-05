import json, os, requests

class CheckForUpdate:
    def __init__(self):
        self.local_version_file = "version.json"
        self.online_version_url = "https://raw.githubusercontent.com/chestnutcapybara/bird-journal-app/main/version.json"
        self.game_folder = "miencraft-game"

    def get_local_version(self):
        if not os.path.exists(self.local_version_file):
            return None
        try:
            with open(self.local_version_file, "r") as f:
                data = json.load(f)
                return data["version"]
        except:
            return None

    def get_online_version(self):
        try:
            r = requests.get(self.online_version_url, timeout=5)
            r.raise_for_status()
            return r.json()["version"]
        except Exception:
            return None
        
    def check_for_updates(self):
        # This is now handled by the thread in main.py, 
        # but kept for compatibility
        self.local = self.get_local_version()
        self.online = self.get_online_version()
        if self.online and self.local != self.online:
            print("Pretending to open updater.exe...")

checkforupdate = CheckForUpdate()
checkforupdate.check_for_updates()