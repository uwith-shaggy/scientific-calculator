import tkinter as tk
import math


def press(key):
    entry_var.set(entry_var.get() + str(key))


def clear():
    entry_var.set("")


def equal():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except:
        entry_var.set("Error")

def scientific(func):
    try:
        value = float(entry_var.get())
        if func == "sqrt":
            entry_var.set(str(math.sqrt(value)))
        elif func == "log":
            entry_var.set(str(math.log(value)))
        elif func == "log10":
            entry_var.set(str(math.log10(value)))
        elif func == "sin":
            entry_var.set(str(math.sin(math.radians(value))))
        elif func == "cos":
            entry_var.set(str(math.cos(math.radians(value))))
        elif func == "tan":
            entry_var.set(str(math.tan(math.radians(value))))
    except:
        entry_var.set("Error")


win = tk.Tk()
win.title("Scientific Calculator")
win.geometry("400x500")
win.resizable(False, False)

entry_var = tk.StringVar()


entry = tk.Entry(win, textvariable=entry_var, font=("Arial", 20), bd=10, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=5, ipadx=8, ipady=15)


buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3), ('sqrt',1,4),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3), ('log',2,4),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3), ('log10',3,4),
    ('0',4,0), ('.',4,1), ('+',4,2), ('=',4,3), ('C',4,4),
    ('sin',5,0), ('cos',5,1), ('tan',5,2), ('(',5,3), (')',5,4)
]


for (text, row, col) in buttons:
    if text == "=":
        b = tk.Button(win, text=text, width=5, height=2, bg="lightgreen", command=equal)
    elif text == "C":
        b = tk.Button(win, text=text, width=5, height=2, bg="red", fg="white", command=clear)
    elif text in ["sqrt", "log", "log10", "sin", "cos", "tan"]:
        b = tk.Button(win, text=text, width=5, height=2, command=lambda t=text: scientific(t))
    else:
        b = tk.Button(win, text=text, width=5, height=2, command=lambda t=text: press(t))
    
    b.grid(row=row, column=col, padx=5, pady=5)

win.mainloop()
