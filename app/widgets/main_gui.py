import tkinter as tk
import random 

from ..parse import parse_json_basic

class Global_gui:
    total_bank = 0

    def __init__(self, window):
        self.window = window
        self.data = parse_json_basic('questions.json')
        self.btn1 = None
        self.btn2 = None
        self.btn3 = None
        self.btn4 = None
        self.level = 14
        self.bank_labels = []
        self.not_in_que = []
        self.question()
        self.buttons()
        self.bank_label()
        self.question_label()
        self.total_cash()


    def buttons(self):
        self.btn1 = tk.Button(self.window, text=self.opt1, bg='#5B6E7A', width=40, height=3, bd=2, relief=tk.SOLID, font=("Arial", 10), command=lambda: self.check_answer(self.btn1))
        self.btn1.place(x=220, y=580)

        self.btn2 = tk.Button(self.window, text=self.opt2, bg='#5B6E7A', width=40, height=3, bd=2, relief=tk.SOLID, font=("Arial", 10), command=lambda: self.check_answer(self.btn2))
        self.btn2.place(x=220, y=480)

        self.btn3 = tk.Button(self.window, text=self.opt3, bg='#5B6E7A', width=40, height=3, bd=2, relief=tk.SOLID, font=("Arial", 10), command=lambda:self.check_answer(self.btn3))
        self.btn3.place(x=720, y=580)

        self.btn4 = tk.Button(self.window, text=self.opt4, bg='#5B6E7A', width=40, height=3, bd=2, relief=tk.SOLID, font=("Arial", 10), command=lambda: self.check_answer(self.btn4))
        self.btn4.place(x=720, y=480)

        take_bank_button = tk.Button(self.window, text='Забрать приз', bg='#5B6E7A', width=10, height=3, bd=1, relief=tk.SOLID, font=("Arial", 10), command=self.take_bank)
        take_bank_button.place(x=25, y=60)

    def question_label(self):
        if hasattr(self, 'question_label_widget') and self.question_label_widget:
            self.question_label_widget.destroy()

        question = tk.Label(self.window, text=self.que, bg='#5B6E7A',fg='white', width=65, height=2, font=("Arial", 20))
        question.place(x=125, y=350)

    def bank_label(self):
        self.bank = [
            '1.000.000', '500.000', '250.000', "125.000",
            "64.000", "32.000", "16.000", "8.000",
            "4.000", "2.000", "1.000", "500",
            "300", "200", "100"
        ]
        self.bank2 = [
            '1000000', '500000', '250000', "125000",
            "64000", "32000", "16000", "8000",
            "4000", "2000", "1000", "500",
            "300", "200", "100"
        ]
        location_y = 10
        for i in self.bank:
            label = tk.Label(self.window, text=i, bg='#10069F',fg='white', width=8, height=1, font=("Arial", 20))
            self.bank_labels.append(label)
            label.place(x=1200, y=location_y)
            location_y +=30

    def total_cash(self):
        total_bank_label = tk.Label(self.window, text=f'Заработано: {Global_gui.total_bank}', bg='#10069F',fg='white', width=20, height=1, font=("Arial", 20))
        total_bank_label.place(x=15, y=10)

    def question(self):
        self.x = random.randint(0, 23)
        while self.x in self.not_in_que:
            self.x = random.randint(0, 23)
        
        que_list = self.data['questions'][self.x]['options']
        random.shuffle(que_list)
        self.que = self.data['questions'][self.x]['text']
        self.anw = self.data['questions'][self.x]['answer']
        self.opt1, self.opt2, self.opt3, self.opt4 = que_list
        self.not_in_que.append(self.x)

    def check_answer(self, name_button):
        if name_button.cget('text') == self.anw:
            name_button.config(bg='green')
            self.buttons_disable()
            self.bank_labels[self.level].config(fg='#FFD700')
            if self.level == 0:
                self.window.after(1000, self.win_window)
            else:
                self.level -= 1
                self.window.after(1000, self.new_que)
        else:
            name_button.config(bg='red')
            self.buttons_disable()
            self.window.after(1000, self.lose_window)

    def new_que(self):
        self.buttons_active()
        self.question()
        self.question_label()
        self.btn1.config(text=self.opt1, bg='#5B6E7A')
        self.btn2.config(text=self.opt2, bg='#5B6E7A')
        self.btn3.config(text=self.opt3, bg='#5B6E7A')
        self.btn4.config(text=self.opt4, bg='#5B6E7A')

    def lose_window(self):
        self.clear_all_widgets()
        lose_bank = tk.Label(self.window, text=f'потеряно 💰{self.bank[self.level]}', bg='#10069F',fg='#FFD700', width=30, height=2, font=("Arial", 25) )
        lose_bank.place(x=375, y=300)
        lose_label = tk.Label(self.window, text='ВЫ ПРОИГРАЛИ', bg='#5B6E7A',fg='white', width=30, height=2, font=("Arial", 30) )
        lose_label.place(x=325, y=200)
        lose_button = tk.Button(self.window, text='Новая игра', bg='#5B6E7A', width=40, height=3, bd=2, relief=tk.SOLID, font=("Arial", 10), command=self.return_game)
        lose_button.place(x=500, y=400)

    def win_window(self):
        self.clear_all_widgets()
        Global_gui.total_bank += int(self.bank2[self.level])
        win_bank = tk.Label(self.window, text=f'Получено 💰{self.bank[self.level]}', bg='#10069F',fg='#FFD700', width=30, height=2, font=("Arial", 25) )
        win_bank.place(x=375, y=300)
        win_label = tk.Label(self.window, text='ВЫ ВЫЙГРАЛИ', bg='#5B6E7A',fg='white', width=30, height=2, font=("Arial", 30) )
        win_label.place(x=325, y=200)
        win_button = tk.Button(self.window, text='Новая игра', bg='#5B6E7A', width=40, height=3, bd=2, relief=tk.SOLID, font=("Arial", 10), command=self.return_game)
        win_button.place(x=500, y=400)

    def take_bank(self):
        if self.level < 14:
            now_bank = self.level + 1
            self.clear_all_widgets()
            Global_gui.total_bank += int(self.bank2[now_bank])
            win_bank = tk.Label(self.window, text=f'Получено 💰{self.bank[now_bank]}', bg='#10069F',fg='#FFD700', width=30, height=2, font=("Arial", 25) )
            win_bank.place(x=375, y=300)
            win_label = tk.Label(self.window, text='ВЫ ВЫЙГРАЛИ', bg='#5B6E7A',fg='white', width=30, height=2, font=("Arial", 30) )
            win_label.place(x=325, y=200)
            win_button = tk.Button(self.window, text='Новая игра', bg='#5B6E7A', width=40, height=3, bd=2, relief=tk.SOLID, font=("Arial", 10), command=self.return_game)
            win_button.place(x=500, y=400)
        else:
            return None


    def return_game(self):
        self.clear_all_widgets()
        Global_gui(self.window)

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

    def clear_all_widgets(self):
        for widget in self.window.winfo_children():
            widget.destroy()