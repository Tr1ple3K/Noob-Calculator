from tkinter import *
import math
def button_press(num):

    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def del_clicked():
    global equation_text

    display = str(equation_text)
    if display == '':
        equation_text = equation_text + '0'
        equation_label.set(equation_text)
        equation_text = ""
    elif display == ' ':
        equation_text = equation_text + '0'
        equation_label.set(equation_text)
        equation_text = ""
    elif display == '0':
        pass
    else:
        equation_text = equation_text[:-1]
        equation_label.set(equation_text)

def equals():

    global equation_text

    try:

        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total

    except SyntaxError:

        equation_label.set("syntax error")

        equation_text = ""

    except ZeroDivisionError:

        equation_label.set("arithmetic error")

        equation_text = ""

   
def clear():

    global equation_text

    equation_label.set("")

    equation_text = ""



window = Tk()
window.title("Calculator program")
window.geometry("424x528")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('Arial',20), bg="#212129", fg="white", width=30, height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, bg="#1D2951",fg="white",text=1, height=3, width=8, font=35,
                 command=lambda: button_press(1))
button1.grid(row=1, column=0)

button2 = Button(frame,bg="#1D2951",fg="white", text=2, height=3, width=8, font=35,
                 command=lambda: button_press(2))
button2.grid(row=1, column=1)

button3 = Button(frame,bg="#1D2951",fg="white", text=3, height=3, width=8, font=35,
                 command=lambda: button_press(3))
button3.grid(row=1, column=2)

button4 = Button(frame,bg="#1D2951",fg="white", text=4, height=3, width=8, font=35,
                 command=lambda: button_press(4))
button4.grid(row=2, column=0)

button5 = Button(frame,bg="#1D2951",fg="white", text=5, height=3, width=8, font=35,
                 command=lambda: button_press(5))
button5.grid(row=2, column=1)

button6 = Button(frame,bg="#1D2951",fg="white", text=6, height=3, width=8, font=35,
                 command=lambda: button_press(6))
button6.grid(row=2, column=2)

button7 = Button(frame,bg="#1D2951",fg="white", text=7, height=3, width=8, font=35,
                 command=lambda: button_press(7))
button7.grid(row=3, column=0)

button8 = Button(frame, bg="#1D2951",fg="white",text=8, height=3, width=8, font=35,
                 command=lambda: button_press(8))
button8.grid(row=3, column=1)

button9 = Button(frame,bg="#1D2951",fg="white", text=9, height=3, width=8, font=35,
                 command=lambda: button_press(9))
button9.grid(row=3, column=2)

button0 = Button(frame,bg="#1D2951",fg="white", text=0, height=3, width=8, font=35,
                 command=lambda: button_press(0))
button0.grid(row=4, column=1)

plus = Button(frame,bg="#1D2951",fg="white", text='+', height=3, width=8, font=35,
                 command=lambda: button_press('+'))
plus.grid(row=0, column=3)

minus = Button(frame, bg="#1D2951",fg="white",text='-', height=3, width=8, font=35,
                 command=lambda: button_press('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, bg="#1D2951",fg="white", text='*', height=3, width=8, font=35,
                 command=lambda: button_press('*'))
multiply.grid(row=2, column=3)

mod = Button(frame, bg="#1D2951",fg="white", text='%', height=3, width=8, font=35,
                 command=lambda: button_press('%'))
mod.grid(row=0, column=2)

divide = Button(frame, bg="#1D2951",fg="white", text='/', height=3, width=8, font=35,
                 command=lambda: button_press('/'))
divide.grid(row=3, column=3)

equal = Button(frame, bg="#E1A95F",fg="white",text='=', height=3, width=8, font=35,
                 command=equals)
equal.grid(row=4, column=3)

decimal = Button(frame,bg="#1D2951",fg="white", text='.', height=3, width=8, font=35,
                 command=lambda: button_press('.'))
decimal.grid(row=4, column=0)

del_btn = Button(frame, text="⌫", command=del_clicked, bg="#1D2951",fg="white", height=3, width=8, font=35)

del_btn.grid(row=4, column=2)

clear = Button(frame,bg="#D21F3C",fg="white", text='C', height=3, width=8, font=35,
                 command=clear)
clear.grid(row=0, column=0)



window.mainloop()