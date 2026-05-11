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
        self.level = 14
        self.bank_labels = []
        self.question()
        self.buttons()
        self.bank_label()
        self.question_label()


    def buttons(self):
        self.btn1 = tk.Button(self.window, text=self.opt1, bg='#5B6E7A', width=40, height=3, bd=2, relief=tk.SOLID, font=("Arial", 10), command=lambda: self.check_answer(self.btn1))
        self.btn1.place(x=220, y=580)

        self.btn2 = tk.Button(self.window, text=self.opt2, bg='#5B6E7A', width=40, height=3, bd=2, relief=tk.SOLID, font=("Arial", 10), command=lambda: self.check_answer(self.btn2))
        self.btn2.place(x=220, y=480)

        self.btn3 = tk.Button(self.window, text=self.opt3, bg='#5B6E7A', width=40, height=3, bd=2, relief=tk.SOLID, font=("Arial", 10), command=lambda:self.check_answer(self.btn3))
        self.btn3.place(x=720, y=580)

        self.btn4 = tk.Button(self.window, text=self.opt4, bg='#5B6E7A', width=40, height=3, bd=2, relief=tk.SOLID, font=("Arial", 10), command=lambda: self.check_answer(self.btn4))
        self.btn4.place(x=720, y=480)

    def question_label(self):
        if hasattr(self, 'question_label_widget') and self.question_label_widget:
            self.question_label_widget.destroy()

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
            label = tk.Label(self.window, text=i, bg='#10069F',fg='white', width=8, height=1, font=("Arial", 20))
            self.bank_labels.append(label)
            label.place(x=1200, y=location_y)
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
            self.buttons_disable()
            self.bank_labels[self.level].config(fg='#FFD700')
            self.level -= 1
            self.window.after(1000, self.new_que)
        else:
            name_button.config(bg='red')
            self.buttons_disable()
            print('Lose')

    def new_que(self):
        self.buttons_active()
        self.question()
        self.question_label()
        self.btn1.config(text=self.opt1, bg='#5B6E7A')
        self.btn2.config(text=self.opt2, bg='#5B6E7A')
        self.btn3.config(text=self.opt3, bg='#5B6E7A')
        self.btn4.config(text=self.opt4, bg='#5B6E7A')

    def buttons_disable(self):
            self.btn1.config(state=tk.DISABLED)
            self.btn2.config(state=tk.DISABLED)
            self.btn3.config(state=tk.DISABLED)
            self.btn4.config(state=tk.DISABLED)

    def buttons_active(self):
            self.btn1.config(state=tk.NORMAL)
            self.btn2.config(state=tk.NORMAL)
            self.btn3.config(state=tk.NORMAL)
            self.btn4.config(state=tk.NORMAL)