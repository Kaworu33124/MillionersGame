import tkinter as tk
import random 

from ..parse import parse_json_basic

class button_setup:
    def __init__(self, window):
        self.window = window
        self.data = parse_json_basic('C:/Users/Admin/Desktop/pyton/millioner/app/questions.json')
        self.btn1 = None  
        self.btn2 = None
        self.btn3 = None
        self.btn4 = None
        self.question()
        self.buttons()
        self.bank_label()
        self.question_label()


    def buttons(self):
        btn1 = tk.Button(self.window, text=self.opt1, bg='#5B6E7A', width=40, height=3, bd=2, relief=tk.SOLID, font=("Arial", 10), command=lambda: self.check_answer(btn1))
        btn1.place(x=220, y=580)

        btn2 = tk.Button(self.window, text=self.opt2, bg='#5B6E7A', width=40, height=3, bd=2, relief=tk.SOLID, font=("Arial", 10), command=lambda: self.check_answer(btn2))
        btn2.place(x=220, y=480)

        btn3 = tk.Button(self.window, text=self.opt3, bg='#5B6E7A', width=40, height=3, bd=2, relief=tk.SOLID, font=("Arial", 10), command=lambda:self.check_answer(btn3))
        btn3.place(x=720, y=580)

        btn4 = tk.Button(self.window, text=self.opt4, bg='#5B6E7A', width=40, height=3, bd=2, relief=tk.SOLID, font=("Arial", 10), command=lambda: self.check_answer(btn4))
        btn4.place(x=720, y=480)

    def question_label(self):
        question = tk.Label(self.window, text=self.que, bg='#5B6E7A',fg='white', width=65, height=2, font=("Arial", 20))
        question.place(x=125, y=350)

    def bank_label(self):
        bank = [
            '1.000.000', '500.000', '250.000', "125.000",
            "64.000", "32.000", "16.000", "8.000",
            "4.000", "2.000", "1.000", "500",
            "300", "200", "100"
        ]
        location_y = 10
        for i in bank:
            i = tk.Label(self.window, text=i, bg='#10069F',fg='white', width=8, height=1, font=("Arial", 20))
            i.place(x=1200, y=location_y)
            location_y +=30

    def question(self):
        self.x = random.randint(1, 10)
        que_list = self.data['questions'][self.x]['options']
        self.que = self.data['questions'][self.x]['text']
        self.anw = self.data['questions'][self.x]['answer']
        self.opt1, self.opt2, self.opt3, self.opt4  = que_list

    def check_answer(self, name_button):
        if name_button.cget('text') == self.anw:
            name_button.config(bg='green')