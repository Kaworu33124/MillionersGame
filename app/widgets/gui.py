import tkinter as tk

from app.widgets.main_gui import global_gui

class Graphics:
    @staticmethod
    def setup(window):
        main_frame = tk.Frame(window,  bg="#10069F")
        main_frame.pack(expand=True, fill="both")
        main_gui = global_gui(main_frame)