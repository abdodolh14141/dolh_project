from tkinter import *
root = Tk()
doc = []
root.title('calculator'.title())
e = Entry(root, width=40, borderwidth=10)
e.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

def click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number)) # type: ignore

def clear():
    e.delete(0, END)

def add():
    first_number = e.get()
    global f_num
    global math
    math = 'addation'
    f_num = int(first_number)
    e.delete(0, END)

def equal():
    secound_num = e.get()
    e.delete(0, END)
    if math == 'addation':
        e.insert(0, f_num + int(secound_num)) # type: ignore
    elif math == 'multiply':
        e.insert(0, f_num * int(secound_num)) # type: ignore
    elif math == 'subtract':
        e.insert(0, f_num - int(secound_num)) # type: ignore
    
def multiply():
    first_number = e.get()
    global f_num
    global math
    math = 'multiply'
    f_num = int(first_number)
    e.delete(0, END)

def subtract():
    first_number = e.get()
    global f_num
    global math
    math = 'subtract'
    f_num = int(first_number)
    e.delete(0, END)

#creat button
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: click(0))
button_add = Button(root, text='+', padx=40, pady=20, command=add)
button_equal = Button(root, text='=', padx=40, pady=20, command=equal)
button_clear = Button(root, text='clear', padx=40, pady=20, command=clear)
button_multiply = Button(root, text='*', padx=40, pady=20, command=multiply)
button_Subtract = Button(root, text='-', padx=40, pady=20, command=subtract)

#show button in screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=4, column=1)
button_equal.grid(row=4, column=2)

button_clear.grid(row=4, column=1)

button_multiply.grid(row=5, column=0)
button_Subtract.grid(row=5, column=1)
button_add.grid(row=5, column=2)
#while loob
root.mainloop()