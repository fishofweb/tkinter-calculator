from tkinter import *

cal = Tk()

cal.title("Basic calculator")
operator = ""

def btnClick(numbers):
    global operator
    operator= operator + str(numbers)
    text_input.set(operator)
def btnClearDisplay():
    global operator
    operator = ""
    text_input.set("")
def equal():
    global operator
    e = str(eval(operator))
    text_input.set(e)
    operator = ""

text_input = StringVar()

textDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable = text_input, insertwidth=10,
 bg="black",fg="white", justify= 'right').grid(columnspan=4)
btn7 = Button(cal, padx=16, fg = "black", font=('arial',20,'bold'),
        text = "7", command=lambda :btnClick(7)).grid(row=1, column=0)

btn8 = Button(cal, padx=16, fg = "black", font=('arial',20,'bold'),
        text = "8", command=lambda :btnClick(8)).grid(row=1, column=1)
btn9 = Button(cal, padx=16, fg = "black", font=('arial',20,'bold'),
        text = "9", command=lambda :btnClick(9)).grid(row=1, column=2)
btn_add = Button(cal,bg="red", padx=16, fg = "black", font=('arial',20,'bold'),
        text = "+", command=lambda :btnClick("+")).grid(row=1, column=3)

btn4 = Button(cal, padx=16, fg = "black", font=('arial',20,'bold'),
        text = "4", command=lambda :btnClick(4)).grid(row=2, column=0)

btn5 = Button(cal, padx=16,  fg = "black", font=('arial',20,'bold'),
        text = "5", command=lambda :btnClick(5)).grid(row=2, column=1)
btn6 = Button(cal, padx=16, fg = "black", font=('arial',20,'bold'),
        text = "6", command=lambda :btnClick(6)).grid(row=2, column=2)
btn_subtract = Button(cal, padx=16,bg="red",fg = "black", font=('arial',20,'bold'),
        text = "-", command=lambda :btnClick("-")).grid(row=2, column=3)

btn1 = Button(cal, padx=16,  fg = "black", font=('arial',20,'bold'),
        text = "1", command=lambda :btnClick(1)).grid(row=3, column=0)

btn2 = Button(cal, padx=16,  fg = "black", font=('arial',20,'bold'),
        text = "2", command=lambda :btnClick(2)).grid(row=3, column=1)
btn3 = Button(cal, padx=16,  fg = "black", font=('arial',20,'bold'),
        text = "3", command=lambda :btnClick(3)).grid(row=3, column=2)
btn_multiply= Button(cal, padx=16,bg="red",fg = "black", font=('arial',20,'bold'),
        text = "*", command=lambda :btnClick("*")).grid(row=3, column=3)

btn0 = Button(cal, padx=16,  fg = "black", font=('arial',20,'bold'),
        text = "0", command=lambda :btnClick(0)).grid(row=4, column=0)
btn_clear = Button(cal, padx=16,bg="blue", fg = "black", font=('arial',20,'bold'),
        text = "Clr", command=btnClearDisplay).grid(row=4, column=1)
btn_equal = Button(cal, padx=16, fg = "black", font=('arial',20,'bold'),
        text = "=",command= equal).grid(row=4, column=2)
btn_divide = Button(cal, padx=16, bg="red",fg = "black", font=('arial',20,'bold'),
        text = "/",command=lambda :btnClick("/")).grid(row=4, column=3)
cal.mainloop()