import customtkinter as ctk
from logic import Logic
from defaults import *

class App(ctk.CTk):
    def __init__(self, logic):
        super().__init__()
        self.logic = logic
        self.title("Better Backpack")
        self.geometry("800x500")
        self.grid_columnconfigure(0, weight=1)

        self.button = Button(self, text="Choose File", command=self.logic.open_file)
        self.button.grid(row=0, column=0, padx=20, pady=20)

def main():
    logic = Logic()
    app = App(logic)
    app.mainloop()

if __name__ == "__main__":
    main()
