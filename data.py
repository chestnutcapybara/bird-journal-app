import json
import os

class BirdData:
    def __init__(self, file="birds.json"):
        self.file = file
        self.birds = self.load()

    def load(self):
        if not os.path.exists(self.file):
            return []

        try:
            with open(self.file, "r") as f:
                return json.load(f)
        except:
            return []

    def save(self):
        with open(self.file, "w") as f:
            json.dump(self.birds, f, indent=4)

    def add_bird(self, name, notes):
        self.birds.append({
            "name": name,
            "notes": notes,
            "favorite": False
        })
        self.save()

    def toggle_favorite(self, index):
        self.birds[index]["favorite"] = not self.birds[index]["favorite"]
        self.save()