import tkinter as tk

from app.widgets.buttons import button_setup

class Graphics:
    @staticmethod
    def setup(window):
        main_frame = tk.Frame(window,  bg="#10069F")
        main_frame.pack(expand=True, fill="both")
        button = button_setup(main_frame)