import customtkinter as ctk
from data import BirdData

if __name__ == '__main__':
    raise RuntimeError("Hey! Don't run app.py (run main.py only)")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Bird Journal 🐦")
        self.geometry("800x600")

        self.data = BirdData()

        self.setup_ui()
        self.refresh_list()

        self.resizable(False, False) # Prevent the user from resizing the window
        # maximize fix
        self.after(0, lambda: self.state("zoomed"))

    def setup_ui(self):
        self.name_entry = ctk.CTkEntry(self, placeholder_text="Bird name")
        self.name_entry.pack(pady=10)

        self.notes_entry = ctk.CTkEntry(self, placeholder_text="Notes")
        self.notes_entry.pack(pady=10)

        self.add_button = ctk.CTkButton(self, text="Add Bird", command=self.add_bird)
        self.add_button.pack(pady=10)

        self.list_frame = ctk.CTkFrame(self)
        self.list_frame.pack(fill="both", expand=True, padx=20, pady=20)

    def add_bird(self):
        name = self.name_entry.get()
        notes = self.notes_entry.get()

        if name:
            self.data.add_bird(name, notes)
            self.refresh_list()

    def refresh_list(self):
        for widget in self.list_frame.winfo_children():
            widget.destroy()

        for i, bird in enumerate(self.data.birds):
            text = f"{bird['name']} ⭐" if bird["favorite"] else bird["name"]

            frame = ctk.CTkFrame(self.list_frame)
            frame.pack(fill="x", pady=5, padx=5)

            label = ctk.CTkLabel(frame, text=text)
            label.pack(side="left", padx=10)

            fav_btn = ctk.CTkButton(
                frame,
                text="★",
                width=40,
                command=lambda i=i: self.toggle_fav(i)
            )
            fav_btn.pack(side="right", padx=10)

    def toggle_fav(self, index):
        self.data.toggle_favorite(index)
        self.refresh_list()