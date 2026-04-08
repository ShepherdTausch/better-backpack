import customtkinter as ctk
from logic import Logic

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title = "Better Backpack"
        self.geometry("800x500")

app = App()
app.mainloop()
