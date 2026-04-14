from tkinter import Tk
from app.widgets.gui import Graphics

class MainWindow:
    def __init__(self):
        self.window = Tk()
        self.window.title("Кто хочет стать миллионером")
        self.window.geometry("1280x720")
        Graphics.setup(self.window)
        self.window.mainloop()