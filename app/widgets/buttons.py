import tkinter as tk

class button_setup:
    def __init__(self, window):
        self.window = window
        self.buttons()
        self.question_label()

    def buttons(self):
        btn1 = tk.Button(self.window, text='', bg='#4c00ff', width=40, height=3, bd=2, relief=tk.SOLID, font=("Arial", 10))
        btn1.place(x=220, y=580)

        btn2 = tk.Button(self.window, text='', bg='#4c00ff', width=40, height=3, bd=2, relief=tk.SOLID, font=("Arial", 10))
        btn2.place(x=220, y=480)

        btn3 = tk.Button(self.window, text='', bg='#4c00ff', width=40, height=3, bd=2, relief=tk.SOLID, font=("Arial", 10))
        btn3.place(x=720, y=580)

        btn4 = tk.Button(self.window, text='', bg='#4c00ff', width=40, height=3, bd=2, relief=tk.SOLID, font=("Arial", 10))
        btn4.place(x=720, y=480)

    def question_label(self):
        question = tk.Label(self.window, text='', bg='#4c00ff',fg='white', width=65, height=2, font=("Arial", 20))
        question.place(x=125, y=350)