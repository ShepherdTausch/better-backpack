import customtkinter as ctk

class Button(ctk.CTkButton):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args, 
            **kwargs, 
            fg_color="#0076ff", 
            hover_color="#278aff",
            corner_radius=32,
            cursor="hand2"
        )

class Sidebar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
