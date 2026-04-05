import customtkinter as ctk
from data import BirdData

from check_for_update import CheckForUpdate

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
    # Add Bird button (always visible)
        self.open_add_btn = ctk.CTkButton(
        self,
        text="➕ Add Bird",
        command=self.toggle_add_menu
    )
        self.open_add_btn.pack(pady=10)
        # MAIN PAGE
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True)

# DETAIL PAGE (hidden at start)
        self.detail_frame = ctk.CTkFrame(self)
    # Add Bird panel (hidden by default)
        self.add_frame = ctk.CTkFrame(self)
    
        self.name_entry = ctk.CTkEntry(self.add_frame, placeholder_text="Bird name")
        self.name_entry.pack(pady=5, padx=10)

        self.notes_entry = ctk.CTkEntry(self.add_frame, placeholder_text="Notes")
        self.notes_entry.pack(pady=5, padx=10)

        self.save_btn = ctk.CTkButton(
        self.add_frame,
        text="Save Bird",
        command=self.add_bird
        )
        self.save_btn.pack(pady=5)

        self.close_btn = ctk.CTkButton(
        self.add_frame,
        text="Cancel",
        command=self.toggle_add_menu
        )
        self.close_btn.pack(pady=5)

    # Bird list
        self.list_frame = ctk.CTkScrollableFrame(self.main_frame)
        self.list_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.add_visible = False

    def toggle_add_menu(self):
        if self.add_visible:
            self.add_frame.pack_forget()
            self.open_add_btn.configure(text="➕ Add Bird")
            self.add_visible = False
        else:
            self.add_frame.pack(pady=10)
            self.open_add_btn.configure(text="✖ Close")
            self.add_visible = True

    def add_bird(self):
        name = self.name_entry.get()
        notes = self.notes_entry.get()

        if name:
            self.data.add_bird(name, notes)
            self.refresh_list()

            # clear inputs
            self.name_entry.delete(0, "end")
            self.notes_entry.delete(0, "end")

            # hide menu after adding
            self.toggle_add_menu()
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
            frame.bind("<Button-1>", lambda e, i=i: self.show_detail(i))
            label.bind("<Button-1>", lambda e, i=i: self.show_detail(i))

    def show_main(self):
        self.detail_frame.pack_forget()
        self.main_frame.pack(fill="both", expand=True)    
    
    def show_detail(self, index):
        bird = self.data.birds[index]

    # hide main page
        self.main_frame.pack_forget()

    # clear old detail page
        for widget in self.detail_frame.winfo_children():
            widget.destroy()

    # build detail page
        title = ctk.CTkLabel(self.detail_frame, text=bird["name"], font=("Arial", 20))
        title.pack(pady=10)

        notes = ctk.CTkLabel(
        self.detail_frame,
        text=bird["notes"],
        wraplength=400
        )
        notes.pack(pady=10)

        fav_text = "⭐ Favorite" if bird["favorite"] else "Not Favorite"
        fav_label = ctk.CTkLabel(self.detail_frame, text=fav_text)
        fav_label.pack(pady=10)

    # back button
        back_btn = ctk.CTkButton(
        self.detail_frame,
        text="← Back",
        command=self.show_main
        )
        back_btn.pack(pady=20)

    # show detail page
        self.detail_frame.pack(fill="both", expand=True)
    def toggle_fav(self, index):
        self.data.toggle_favorite(index)
        self.refresh_list()