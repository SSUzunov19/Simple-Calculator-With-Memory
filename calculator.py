from tkinter import Tk, Entry, Button, StringVar
from math import sqrt, factorial

class Calculator:
    def __init__(self, master):
        self.master = master
        self.expression = ""
        self.memory = ""
        self.master.title("Calculator")
        self.calc_box = StringVar()
        self.calc_field = Entry(master, textvariable=self.calc_box, font=("Helvetica", 28), width=18, bd=0, justify='right')
        self.calc_field.grid(row=0, column=0, columnspan=6, padx=4, pady=4)

        keys = ['M/EX', 'M+', 'M-', 'MR', 'MC', 'GT',
                'AC', '7', '8', '9', '%', '√', 
                '+/-', '4', '5', '6', '*', '/',
                'DEL', '1', '2', '3', '+', '-',
                'CE', '0', '00', '.', '!', '=']

        self.buttons = []
        n = 0
        for c in keys:
            button = Button(master, text=c, command=lambda c=c: self.calc_action(c), font=("Helvetica 18"), width=7)
            button.grid(row=2+n//6, column=n%6)
            self.buttons.append(button)
            n += 1

    def calc_action(self, key):
        if key == 'AC':
            self.expression = ""
        elif key == 'DEL':
            self.expression = self.expression[:-1]
        elif key == 'CE':
            self.calc_box.set("")
            self.expression = ""
        elif key == 'GT':
            try:
                self.expression = str(float(self.memory))
            except:
                self.expression = "Error"
        elif key == '√':
            try:
                value = float(self.expression)
                if value < 0:
                    self.expression = "Error"
                else:
                    self.expression = str(sqrt(value))
            except:
                self.expression = "Error"
        elif key == '!':
            self.expression = str(factorial(int(float(self.expression))))
        elif key == '+/-':
            self.expression = str(float(self.expression) * -1)
        elif key == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception as e:
                self.expression = "Error"
        elif key == 'M/EX':
            self.memory = self.expression
            self.expression = ""
        elif key == 'M+':
            try:
                self.memory = str(float(self.memory) + float(self.calc_box.get()))
                self.expression = ""
            except:
                self.expression = "Error"
        elif key == 'M-':
            try:
                self.memory = str(float(self.memory) - float(self.calc_box.get()))
                self.expression = ""
            except:
                self.expression = "Error"
        elif key == 'MR':
            self.expression = self.memory
        elif key == 'MC':
            self.memory = ""
        else:
            if self.expression == "Error":
                self.expression = ""
            self.expression += key

        self.calc_box.set(self.expression)


root = Tk()
game = Calculator(root)
root.mainloop()
