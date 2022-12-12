#Pattanapong Chirabandhu 6310742132

from decimal import Decimal
from tkinter import *
import tkinter
import math
from tkinter import scrolledtext

root = Tk()
root.geometry("800x580")
root.title("Calculator")

#History Window
def openHistory():  
    historyRoot = Tk()
    historyRoot.geometry("400x700")
    historyRoot.title("History")
    historyRoot.configure(bg='black') #set background color
    st = scrolledtext.ScrolledText(historyRoot, width=50, height=10, bg="white",fg="black")

    #Refresh history for new data
    def refreshHistory():
        st.delete("1.0","end")
        with open("calculatorHistory.txt","r") as file:
            st.insert(tkinter.INSERT, file.read())
            #always look at bottom of screen when press refresh button
            st.mark_set("insert", "50.1") 
            st.see("insert")

    #Delete all data in history file
    def deleteHistory():
        st.delete("1.0","end")
        with open("calculatorHistory.txt","r+") as file:
            file.truncate(0)
    
    Label(historyRoot, text="Calculator History",font="Arial 14 bold",fg="white",bg="black").pack(pady=(20,0))
    with open("calculatorHistory.txt","r") as file:
        st.insert(tkinter.INSERT, file.read())  

    buttonFrame = Frame(historyRoot,bg="black")
    buttonFrame.pack(pady=(20,0))
    refreshButton = Button(buttonFrame, text="Refresh", command=refreshHistory,bd=0, bg="#C1A225", fg="white", height=1, width=15,activebackground="#5072A7",activeforeground="white")
    refreshButton.pack(side=LEFT, padx=(0,20)) # set to middle padding from top 40 units
    deleteButton = Button(buttonFrame, text="Delete", command=deleteHistory,bd=0, bg="#D21F3C", fg="white", height=1, width=15,activebackground="#5072A7",activeforeground="white")
    deleteButton.pack(side=LEFT) # 

    st.pack(pady=(20,0),fill=tkinter.BOTH, side=tkinter.LEFT, expand=True)

# create a toplevel menu  
menubar = Menu(root)  
menubar.add_command(label="History", command=openHistory)  

#Color theme
def blue():
    color = "#1D2951"
    white = "white"
    resultBox.configure(bg="black")
    buttonC.configure(bg="#D21F3C")
    buttonMod.configure(bg=color,fg=white)
    buttonFactorial.configure(bg=color,fg=white)
    buttonDivide.configure(bg=color,fg= white)
    buttonSin.configure(bg=color,fg= white)
    buttonCos.configure(bg=color,fg=white)
    buttonTan.configure(bg=color,fg= white) 
    button1.configure(bg=color,fg= white)
    button2.configure(bg=color,fg= white)
    button3.configure(bg=color,fg= white)
    buttonMultiply.configure(bg=color,fg= white)
    buttonAsin.configure(bg=color,fg= white)
    buttonAcos.configure(bg=color,fg= white)
    buttonAtan.configure(bg=color,fg= white)
    button4.configure(bg=color,fg= white) 
    button5.configure(bg=color,fg= white) 
    button6.configure(bg=color,fg= white) 
    buttonSubtract.configure(bg=color,fg= white) 
    buttonLn.configure(bg=color,fg= white)
    buttonLog.configure(bg=color,fg= white) 
    buttonPower.configure(bg=color,fg= white)
    button7.configure(bg=color,fg= white) 
    button8.configure(bg=color,fg= white)
    button9.configure(bg=color,fg= white) 
    buttonPlus.configure(bg=color,fg= white)
    buttonRound.configure(bg=color,fg= white)
    buttonBracketL.configure(bg=color,fg= white)
    buttonBracketR.configure(bg=color,fg=white) 
    buttonDot.configure(bg=color,fg= white) 
    button0.configure(bg=color,fg= white)
    buttonDelete.configure(bg=color,fg= white) 
    buttonEqual.configure(bg="#C1A225")
    buttonPi.configure(bg=color,fg= white)
    buttonE.configure(bg=color,fg= white) 
    buttonSqr.configure(bg=color,fg= white)
    
def green():
    color = "#097969"
    white = "white"
    resultBox.configure(bg="black")
    buttonC.configure(bg="#D21F3C")
    buttonMod.configure(bg=color,fg= white)
    buttonFactorial.configure(bg=color,fg= white)
    buttonDivide.configure(bg=color,fg= white)
    buttonSin.configure(bg=color,fg= white)
    buttonCos.configure(bg=color,fg= white)
    buttonTan.configure(bg=color,fg= white) 
    button1.configure(bg=color,fg= white)
    button2.configure(bg=color,fg= white)
    button3.configure(bg=color,fg= white)
    buttonMultiply.configure(bg=color,fg= white)
    buttonAsin.configure(bg=color,fg= white)
    buttonAcos.configure(bg=color,fg= white)
    buttonAtan.configure(bg=color,fg= white)
    button4.configure(bg=color,fg= white) 
    button5.configure(bg=color,fg= white) 
    button6.configure(bg=color,fg= white) 
    buttonSubtract.configure(bg=color,fg= white) 
    buttonLn.configure(bg=color,fg= white)
    buttonLog.configure(bg=color,fg= white) 
    buttonPower.configure(bg=color,fg= white)
    button7.configure(bg=color,fg= white) 
    button8.configure(bg=color,fg= white)
    button9.configure(bg=color,fg= white) 
    buttonPlus.configure(bg=color,fg= white)
    buttonRound.configure(bg=color,fg= white)
    buttonBracketL.configure(bg=color,fg= white)
    buttonBracketR.configure(bg=color,fg= white) 
    buttonDot.configure(bg=color,fg= white) 
    button0.configure(bg=color,fg= white)
    buttonDelete.configure(bg=color,fg= white) 
    buttonEqual.configure(bg="#C1A225")
    buttonPi.configure(bg=color,fg= white)
    buttonE.configure(bg=color,fg= white) 
    buttonSqr.configure(bg=color,fg= white)

def purple():
    color = "#9370DB"
    white = "white"
    resultBox.configure(bg="black")
    buttonC.configure(bg="#D21F3C")
    buttonMod.configure(bg=color,fg= white)
    buttonFactorial.configure(bg=color,fg= white)
    buttonDivide.configure(bg=color,fg= white)
    buttonSin.configure(bg=color,fg= white)
    buttonCos.configure(bg=color,fg= white)
    buttonTan.configure(bg=color,fg= white) 
    button1.configure(bg=color,fg= white)
    button2.configure(bg=color,fg= white)
    button3.configure(bg=color,fg= white)
    buttonMultiply.configure(bg=color,fg= white)
    buttonAsin.configure(bg=color,fg= white)
    buttonAcos.configure(bg=color,fg= white)
    buttonAtan.configure(bg=color,fg= white)
    button4.configure(bg=color,fg= white) 
    button5.configure(bg=color,fg= white) 
    button6.configure(bg=color,fg= white) 
    buttonSubtract.configure(bg=color,fg= white) 
    buttonLn.configure(bg=color,fg= white)
    buttonLog.configure(bg=color,fg= white) 
    buttonPower.configure(bg=color,fg= white)
    button7.configure(bg=color,fg= white) 
    button8.configure(bg=color,fg= white)
    button9.configure(bg=color,fg= white) 
    buttonPlus.configure(bg=color,fg= white)
    buttonRound.configure(bg=color,fg= white)
    buttonBracketL.configure(bg=color,fg= white)
    buttonBracketR.configure(bg=color,fg= white) 
    buttonDot.configure(bg=color,fg= white) 
    button0.configure(bg=color,fg= white)
    buttonDelete.configure(bg=color,fg= white) 
    buttonEqual.configure(bg="#C1A225")
    buttonPi.configure(bg=color,fg= white)
    buttonE.configure(bg=color,fg= white) 
    buttonSqr.configure(bg=color,fg= white)
    
def vividOrange():
    color = "#FF5E0E"
    white = "white"
    resultBox.configure(bg="black")
    buttonC.configure(bg="#D21F3C")
    buttonMod.configure(bg=color,fg= white)
    buttonFactorial.configure(bg=color,fg= white)
    buttonDivide.configure(bg=color,fg= white)
    buttonSin.configure(bg=color,fg= white)
    buttonCos.configure(bg=color,fg= white)
    buttonTan.configure(bg=color,fg= white) 
    button1.configure(bg=color,fg= white)
    button2.configure(bg=color,fg= white)
    button3.configure(bg=color,fg= white)
    buttonMultiply.configure(bg=color,fg= white)
    buttonAsin.configure(bg=color,fg= white)
    buttonAcos.configure(bg=color,fg= white)
    buttonAtan.configure(bg=color,fg= white)
    button4.configure(bg=color,fg= white) 
    button5.configure(bg=color,fg= white) 
    button6.configure(bg=color,fg= white) 
    buttonSubtract.configure(bg=color,fg= white) 
    buttonLn.configure(bg=color,fg= white)
    buttonLog.configure(bg=color,fg= white) 
    buttonPower.configure(bg=color,fg= white)
    button7.configure(bg=color,fg= white) 
    button8.configure(bg=color,fg= white)
    button9.configure(bg=color,fg= white) 
    buttonPlus.configure(bg=color,fg= white)
    buttonRound.configure(bg=color,fg= white)
    buttonBracketL.configure(bg=color,fg= white)
    buttonBracketR.configure(bg=color,fg= white) 
    buttonDot.configure(bg=color,fg= white) 
    button0.configure(bg=color,fg= white)
    buttonDelete.configure(bg=color,fg= white) 
    buttonEqual.configure(bg="#C1A225")
    buttonPi.configure(bg=color,fg= white)
    buttonE.configure(bg=color,fg= white) 
    buttonSqr.configure(bg=color,fg= white)

def blackAndWhite():
    black="#000000"
    white="#FFFFFF"
    resultBox.configure(bg=black)
    buttonC.configure(bg=black)
    buttonMod.configure(bg=white, fg=black)
    buttonFactorial.configure(bg=white, fg=black)
    buttonDivide.configure(bg=white, fg=black)
    buttonSin.configure(bg=white, fg=black)
    buttonCos.configure(bg=white, fg=black)
    buttonTan.configure(bg=white, fg=black)
    button1.configure(bg=white, fg=black)
    button2.configure(bg=white, fg=black)
    button3.configure(bg=white, fg=black)
    buttonMultiply.configure(bg=white, fg=black)
    buttonAsin.configure(bg=white, fg=black)
    buttonAcos.configure(bg=white, fg=black)
    buttonAtan.configure(bg=white, fg=black)
    button4.configure(bg=white, fg=black)
    button5.configure(bg=white, fg=black)
    button6.configure(bg=white, fg=black)
    buttonSubtract.configure(bg=white, fg=black)
    buttonLn.configure(bg=white, fg=black)
    buttonLog.configure(bg=white, fg=black)
    buttonPower.configure(bg=white, fg=black)
    button7.configure(bg=white, fg=black)
    button8.configure(bg=white, fg=black)
    button9.configure(bg=white, fg=black)
    buttonPlus.configure(bg=white, fg=black)
    buttonRound.configure(bg=white, fg=black)
    buttonBracketL.configure(bg=white, fg=black)
    buttonBracketR.configure(bg=white, fg=black)
    buttonDot.configure(bg=white, fg=black)
    button0.configure(bg=white, fg=black)
    buttonDelete.configure(bg=white, fg=black)
    buttonEqual.configure(bg=black)
    buttonPi.configure(bg=white, fg=black)
    buttonE.configure(bg=white, fg=black)
    buttonSqr.configure(bg=white, fg=black)

#Menu bar
colorMenu = Menu(menubar, tearoff=0)
colorMenu.add_command(label="Blue", command=blue)  
colorMenu.add_command(label="Green", command=green)  
colorMenu.add_command(label="Purple", command=purple)  
colorMenu.add_command(label="Vivid orange", command=vividOrange) 
colorMenu.add_command(label="Black&White", command=blackAndWhite) 
menubar.add_cascade(label="Settings", menu=colorMenu)

# display the menu  
#Every time when user pressed a button it will check if there's "Syntax Error" showing on display. if yes then delete that word
root.config(menu=menubar)  
  
def buttonClear_click():
    resultBox.delete(0, END)
    resultBox.insert(0, '0')

def button1_click():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    if resultBox.get() == '0':
        resultBox.delete(0, END)
    pos = len(resultBox.get())
    resultBox.insert(pos, '1')

def button2_click():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    if resultBox.get() == '0':
        resultBox.delete(0, END)
    pos = len(resultBox.get())
    resultBox.insert(pos, '2')

def button3_click():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    if resultBox.get() == '0':
        resultBox.delete(0, END)
    pos = len(resultBox.get())
    resultBox.insert(pos, '3')

def button4_click():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    if resultBox.get() == '0':
        resultBox.delete(0, END)
    pos = len(resultBox.get())
    resultBox.insert(pos, '4')

def button5_click():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    if resultBox.get() == '0':
        resultBox.delete(0, END)
    pos = len(resultBox.get())
    resultBox.insert(pos, '5')

def button6_click():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    if resultBox.get() == '0':
        resultBox.delete(0, END)
    pos = len(resultBox.get())
    resultBox.insert(pos, '6')

def button7_click():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    if resultBox.get() == '0':
        resultBox.delete(0, END)
    pos = len(resultBox.get())
    resultBox.insert(pos, '7')

def button8_click():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    if resultBox.get() == '0':
        resultBox.delete(0, END)
    pos = len(resultBox.get())
    resultBox.insert(pos, '8')

def button9_click():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    if resultBox.get() == '0':
        resultBox.delete(0, END)
    pos = len(resultBox.get())
    resultBox.insert(pos, '9')

def button0_click():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    if resultBox.get() == '0':
        resultBox.delete(0, END)
    pos = len(resultBox.get())
    resultBox.insert(pos, '0')

def plus_click():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    pos = len(resultBox.get())
    resultBox.insert(pos, '+')

def sub_click():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    pos = len(resultBox.get())
    resultBox.insert(pos, '-')

def multiply_click():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    pos = len(resultBox.get())
    resultBox.insert(pos, '*')

def mod_click():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    pos = len(resultBox.get())
    resultBox.insert(pos, '%')

def divide_click():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    pos = len(resultBox.get())
    resultBox.insert(pos, '/')

def fact_click():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    try:
        data = int(resultBox.get())
        ans = math.factorial(data)
        formatCheck(ans)
        writeFile(ans,data)
    except Exception:
        showError()

#For decimal number
def dot_click():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    pos = len(resultBox.get())
    resultBox.insert(pos, '.')

#Delete current number on display
def delete_clicked():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    pos = len(resultBox.get())
    display = str(resultBox.get())
    if display == '':
        resultBox.insert(0, '0')
    elif display == '0':
        pass
    else:
        resultBox.delete(0, END)
        resultBox.insert(0, display[0:pos-1])

def equal_click():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    try:
        data = str(resultBox.get())
        ans = eval(data)
        formatCheck(ans)
        writeFile(ans,data)
    except:
        showError()

def sin_click():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    try:
        data = float(resultBox.get())
        ans = math.sin(data)
        resultBox.delete(0, END)
        resultBox.insert(0, str(ans))
        name = 'sin'
        writeFile2(ans,data,name)
    except Exception:
        showError()

def cos_click():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    try:
        data = float(resultBox.get())
        ans = math.cos(data)
        resultBox.delete(0, END)
        resultBox.insert(0, str(ans))
        name = 'cos'
        writeFile2(ans,data,name)
    except Exception:
        showError()

def tan_click():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    try:
        data = float(resultBox.get())
        ans = math.tan(data)
        resultBox.delete(0, END)
        resultBox.insert(0, str(ans))
        name = 'tan'
        writeFile2(ans,data,name)
    except Exception:
        showError()

def arcsin_click():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    try:
        data = float(resultBox.get())
        ans = math.asin(data)
        resultBox.delete(0, END)
        resultBox.insert(0, str(ans))
        name = 'arcsin'
        writeFile2(ans,data,name)
    except Exception:
        showError()

def arccos_click():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    try:
        data = float(resultBox.get())
        ans = math.acos(data)
        resultBox.delete(0, END)
        resultBox.insert(0, str(ans))
        name = 'arccos'
        writeFile2(ans,data,name)
    except Exception:
        showError()

def arctan_click():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    try:
        data = float(resultBox.get())
        ans = math.atan(data)
        resultBox.delete(0, END)
        resultBox.insert(0, str(ans))
        name = 'arctan'
        writeFile2(ans,data,name)
    except Exception:
        showError()

def ln_clicked():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    try:
        data = float(resultBox.get())
        ans = math.log(data)
        resultBox.delete(0, END)
        resultBox.insert(0, str(ans))
        name = 'ln'
        writeFile2(ans,data,name)
    except Exception:
        showError()

def logarithm_click():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    try:
        data = float(resultBox.get())
        ans = math.log10(data)
        resultBox.delete(0, END)
        resultBox.insert(0, str(ans))
        name = 'log'
        writeFile2(ans,data,name)
    except Exception:
        showError()
      
def pow_click():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    pos = len(resultBox.get())
    resultBox.insert(pos, '**')

def round_click():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    try:
        data = float(resultBox.get())
        ans = round(data)
        formatCheck(ans)
        writeFile(ans,data)
    except Exception:
        showError()

def bracketl_click():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    if resultBox.get() == '0':
        resultBox.delete(0, END)
    pos = len(resultBox.get())
    resultBox.insert(pos, '(')

def bracketr_click():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    if resultBox.get() == '0':
        resultBox.delete(0, END)
    pos = len(resultBox.get())
    resultBox.insert(pos, ')')

def pi_click():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    if resultBox.get() == '0':
        resultBox.delete(0, END)
    pos = len(resultBox.get())
    resultBox.insert(pos, str(math.pi))

def e_click():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    if resultBox.get() == '0':
        resultBox.delete(0, END)
    pos = len(resultBox.get())
    resultBox.insert(pos, str(math.e))

def sqr_click():
    if resultBox.get() == 'Syntax Error':
        resultBox.delete(0, END)
    try:
        data = float(resultBox.get())
        ans = math.sqrt(data)
        formatCheck(ans)
        writeFile(ans,data)
    except Exception:
        showError()

#if num length more than 30 then convert to scientific e notation
def formatCheck(ans):
    if len(str(ans)) >= 30:
            resultBox.delete(0, END)
            resultBox.insert(0, '%.2E' % Decimal(ans))
    else: #if it's not insert normally
        resultBox.delete(0, END)
        resultBox.insert(0, ans)

#if it error show a error message
def showError():
    resultBox.delete(0, END)
    resultBox.insert(0, "Syntax Error")

#This function is for wwrite a result to file for example equal button 
def writeFile(ans, data):
    with open("calculatorHistory.txt", 'a') as file:
        if len(str(ans)) >= 30:
           result = str('%.2E' % Decimal(ans)) #this is for convert to scientific e notation 
           file.write(f'{data} = {result}\n')
        else:
            result = str(ans)
            file.write(f'{data} = {result}\n')
        file.close()

#This function is for write a result to file for example sin cos tan arcsin arccos arctan log ln button etc. 
def writeFile2(ans, data, name):
    with open("calculatorHistory.txt", 'a') as file:
        if len(str(ans)) >= 30:
           result = str('%.2E' % Decimal(ans)) #this is for convert to scientific e notation 
           file.write(f'{name}({data}) = {result}\n')
        else:
            result = str(ans)
            file.write(f'{name}({data}) = {result}\n')
        file.close()

color = "#1D2951"
#This is main entry box **Very important**
resultBox = Entry(root, font="Arial 20",bd = 0, fg="white", bg="black", justify=CENTER, insertbackground="#000000", cursor="arrow")
resultBox.pack(expand=TRUE, fill=BOTH)

#Below all of this using pack for place a button row by row, new button always add to left
# Row 1 Buttons
row1 = Frame(root, bg="#000000")
buttonC = Button(row1, text="C", font="Arial 20", padx=5, pady=5,relief=RAISED, bd=1, command=buttonClear_click, fg="white", bg="#D21F3C")
buttonMod = Button(row1, text="%", font="Arial 20", padx=5, pady=5,relief=GROOVE, bd=0, command=mod_click, fg="white", bg=color)
buttonFactorial = Button(row1, text=" x! ", font="Arial 18", padx=5, pady=5,relief=GROOVE, bd=0, command=fact_click, fg="white", bg=color)
buttonDivide = Button(row1, text="÷", font="Arial 25",  padx=5, pady=5, relief=GROOVE, bd=0, command=divide_click, fg="white", bg=color)
buttonSin = Button(row1, text="sin", font="Arial 15", padx=5, pady=5,relief=GROOVE, bd=0, command=sin_click, fg="white", bg=color)
buttonCos = Button(row1, text="cos", font="Arial 15", padx=5, pady=5,relief=GROOVE, bd=0, command=cos_click, fg="white", bg=color)
buttonTan = Button(row1, text="tan", font="Arial 15", padx=5, pady=5,relief=GROOVE, bd=0, command=tan_click, fg="white", bg=color)

row1.pack(expand=TRUE, fill=BOTH)
buttonC.pack(side=LEFT, expand=TRUE, fill=BOTH)
buttonMod.pack(side=LEFT, expand=TRUE, fill=BOTH)
buttonFactorial.pack(side=LEFT, expand=TRUE, fill=BOTH)
buttonDivide.pack(side=LEFT, expand=TRUE, fill=BOTH)
buttonSin.pack(side=LEFT, expand=TRUE, fill=BOTH)
buttonCos.pack(side=LEFT, expand=TRUE, fill=BOTH)
buttonTan.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 2 Buttons
row2 = Frame(root)
button1 = Button(row2, text="1", font="Arial 20", padx=5, pady=5,relief=GROOVE, bd=0, command=button1_click, fg="white", bg=color)
button2 = Button(row2, text="2", font="Arial 20", padx=5, pady=5,relief=GROOVE, bd=0,  command=button2_click, fg="white", bg=color)
button3 = Button(row2, text="3", font="Arial 20", padx=5, pady=5,relief=GROOVE, bd=0, command=button3_click, fg="white", bg=color)
buttonMultiply = Button(row2, text="x", font="Arial 21",padx=5, pady=5, relief=GROOVE, bd=0, command=multiply_click, fg="white", bg=color)
buttonAsin = Button(row2, text="asin", font="Arial 9", padx=5, pady=5,relief=GROOVE, bd=0, command=arcsin_click, fg="white", bg=color)
buttonAcos = Button(row2, text="acos", font="Arial 10", padx=5, pady=5,relief=GROOVE, bd=0, command=arccos_click, fg="white", bg=color)
buttonAtan = Button(row2, text="atan", font="Arial 10", padx=5, pady=5,relief=GROOVE, bd=0, command=arctan_click, fg="white", bg=color)

row2.pack(expand=TRUE, fill=BOTH)
button1.pack(side=LEFT, expand=TRUE, fill=BOTH)
button2.pack(side=LEFT, expand=TRUE, fill=BOTH)
button3.pack(side=LEFT, expand=TRUE, fill=BOTH)
buttonMultiply.pack(side=LEFT, expand=TRUE, fill=BOTH)
buttonAsin.pack(side=LEFT, expand=TRUE, fill=BOTH)
buttonAcos.pack(side=LEFT, expand=TRUE, fill=BOTH)
buttonAtan.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 3 Buttons
row3 = Frame(root)
button4 = Button(row3, text="4", font="Arial 20", padx=5, pady=5,relief=GROOVE, bd=0, command=button4_click, fg="white", bg=color)
button5 = Button(row3, text="5", font="Arial 20", padx=5, pady=5,relief=GROOVE, bd=0, command=button5_click, fg="white", bg=color)
button6 = Button(row3, text="6", font="Arial 20", padx=5, pady=5,relief=GROOVE, bd=0, command=button6_click, fg="white", bg=color)
buttonSubtract = Button(row3, text="-", font="Arial 23", padx=5, pady=5,relief=GROOVE, bd=0, command=sub_click, fg="white", bg=color)
buttonLn = Button(row3, text="ln", font="Arial 14", padx=5, pady=5,relief=GROOVE, bd=0, command=ln_clicked, fg="white", bg=color)
buttonLog = Button(row3, text="log", font="Arial 14", padx=5, pady=5,relief=GROOVE, bd=0, command=logarithm_click, fg="white", bg=color)
buttonPower = Button(row3, text="x^y", font="Arial 12", padx=5, pady=5,relief=GROOVE, bd=0, command=pow_click, fg="white", bg=color)

row3.pack(expand=TRUE, fill=BOTH)
button4.pack(side=LEFT, expand=TRUE, fill=BOTH)
button5.pack(side=LEFT, expand=TRUE, fill=BOTH)
button6.pack(side=LEFT, expand=TRUE, fill=BOTH)
buttonSubtract.pack(side=LEFT, expand=TRUE, fill=BOTH)
buttonLn.pack(side=LEFT, expand=TRUE, fill=BOTH)
buttonLog.pack(side=LEFT, expand=TRUE, fill=BOTH)
buttonPower.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 4 Buttons
row4 = Frame(root)
button7 = Button(row4, text="7", font="Arial 20", padx=5, pady=5,relief=GROOVE, bd=0, command=button7_click, fg="white", bg=color)
button8 = Button(row4, text="8", font="Arial 20", padx=5, pady=5,relief=GROOVE, bd=0, command=button8_click, fg="white", bg=color)
button9 = Button(row4, text="9", font="Arial 20",padx=5, pady=5, relief=GROOVE, bd=0, command=button9_click, fg="white", bg=color)
buttonPlus = Button(row4, text="+", font="Arial 19",padx=5, pady=5, relief=GROOVE, bd=0, command=plus_click, fg="white", bg=color)
buttonRound = Button(row4, text="Rnd", font="Arial 8 bold", padx=5, pady=5,relief=GROOVE, bd=0, command=round_click, fg="white", bg=color)
buttonBracketL = Button(row4, text=" ( ", font="Arial 17", padx=5, pady=5,relief=GROOVE, bd=0, command=bracketl_click, fg="white", bg=color)
buttonBracketR = Button(row4, text=" ) ", font="Arial 15", padx=5, pady=5,relief=GROOVE, bd=0, command=bracketr_click, fg="white", bg=color)

row4.pack(expand=TRUE, fill=BOTH)
button7.pack(side=LEFT, expand=TRUE, fill=BOTH)
button8.pack(side=LEFT, expand=TRUE, fill=BOTH)
button9.pack(side=LEFT, expand=TRUE, fill=BOTH)
buttonPlus.pack(side=LEFT, expand=TRUE, fill=BOTH)
buttonRound.pack(side=LEFT, expand=TRUE, fill=BOTH)
buttonBracketL.pack(side=LEFT, expand=TRUE, fill=BOTH)
buttonBracketR.pack(side=LEFT, expand=TRUE, fill=BOTH)

#Row 5 Buttons
row5 = Frame(root)
buttonDot = Button(row5, text=".", font="Arial 20", padx=5, pady=5,relief=GROOVE, bd=0, command=dot_click, fg="white", bg=color)
button0 = Button(row5, text="0", font="Arial 20", padx=5, pady=5,relief=GROOVE, bd=0, command=button0_click, fg="white", bg=color)
buttonDelete = Button(row5, text="⌫", font="Arial 12", padx=5, pady=5,relief=GROOVE, bd=0, command=delete_clicked, fg="white", bg=color)
buttonEqual = Button(row5, text="=", font="Arial 17", padx=5, pady=5,relief=RAISED, bd=1, command=equal_click, fg="white", bg="#C1A225")
buttonPi = Button(row5, text="π", font="Arial 14", padx=5, pady=5,relief=GROOVE, bd=0, command=pi_click, fg="white", bg=color)
buttonE = Button(row5, text="e", font="Arial 19", padx=5, pady=5,relief=GROOVE, bd=0, command=e_click, fg="white", bg=color)
buttonSqr = Button(row5, text=" √x ", font="Arial 10",padx=5, pady=5,relief=GROOVE, bd=0, command=sqr_click, fg="white", bg=color)

row5.pack(expand=TRUE, fill=BOTH)
buttonDot.pack(side=LEFT, expand=TRUE, fill=BOTH)
button0.pack(side=LEFT, expand=TRUE, fill=BOTH)
buttonDelete.pack(side=LEFT, expand=TRUE, fill=BOTH)
buttonEqual.pack(side=LEFT, expand=TRUE, fill=BOTH)
buttonPi.pack(side=LEFT, expand=TRUE, fill=BOTH)
buttonE.pack(side=LEFT, expand=TRUE, fill=BOTH)
buttonSqr.pack(side=LEFT, expand=TRUE, fill=BOTH)

#For running gui 
root.mainloop()