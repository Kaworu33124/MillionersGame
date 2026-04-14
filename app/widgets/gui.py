import tkinter as tk
import CTkGradient as ctkg

class Graphics:
    @staticmethod
    def setup(window):
        main_frame = tk.Frame(window)
        main_frame.pack(expand=True, fill="both")
        gradient_bg = ctkg.GradientFrame(master=main_frame, colors=('#4c00ff', '#0033ff'), direction="vertical", corner_radius=0, height=50, width=50)
        gradient_bg.pack(expand=True, fill="both")