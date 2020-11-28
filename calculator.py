from tkinter import *

root = Tk()
root.title("Kays New Calculator ")

app_width = Entry(root, width = 40, borderwidth = 5)

app_width.grid(row = 0, column = 0, columnspan = 3, padx = 12, pady = 20)
## button click def
def button_click(number):
    current = app_width.get()
    app_width.delete(0,END)
    app_width.insert(0, str(current) + str(number))

## clear def
def clear_def():
    app_width.delete(0,END)

## sum def 
def sum():
    first_num = app_width.get()
    global f_num
    global math
    math = "sum"
    f_num = first_num
    app_width.delete(0,END)
    

## equal def
def equal():
    second_number = app_width.get()
    app_width.delete(0,END)
    if math == "sum":
        app_width.insert(0,f_num + second_number)
    if math == "minus":
        app_width.insert(0,f_num - second_number)
    if math == "multiply":
        app_width.insert(0,f_num * second_number)
    if math == "divided":
        app_width.insert(0,f_num/ second_number)

## minus def
def minus():
    first_num = app_width.get()
    global f_num
    global math
    math = "minus"
    f_num = first_num
    app_width.delete(0,END)
## multiply def 
def multiply():
    first_num = app_width.get()
    global f_num
    global math
    math = "multiply"
    f_num = first_num
    app_width.delete(0,END)
# divided def 
def divided():
    first_num = app_width.get()
    global f_num
    global math
    math = "divided"
    f_num = first_num
    app_width.delete(0,END)

## number button
num_1 = Button(root,text = "1", padx = 40, pady = 20, command = lambda: button_click(1) )
num_2 = Button(root,text = "2", padx = 40, pady = 20, command = lambda: button_click(2) )
num_3 = Button(root,text = "3", padx = 40, pady = 20, command = lambda: button_click(3) )
num_4 = Button(root,text = "4", padx = 40, pady = 20, command = lambda: button_click(4) )
num_5 = Button(root,text = "5", padx = 40, pady = 20, command = lambda: button_click(5) )
num_6 = Button(root,text = "6", padx = 40, pady = 20, command = lambda: button_click(6) )
num_7 = Button(root,text = "7", padx = 40, pady = 20, command = lambda: button_click(7) )
num_8 = Button(root,text = "8", padx = 40, pady = 20, command = lambda: button_click(8) )
num_9 = Button(root,text = "9", padx = 40, pady = 20, command = lambda: button_click(9) )
num_0 = Button(root,text = "0", padx = 40, pady = 20, command = lambda: button_click(0) )

## symble button
num_add = Button(root,text = "+", padx = 40, pady = 20, command = sum )
num_minus = Button(root,text = "-", padx = 40, pady = 20, command = minus )
num_multiply = Button(root,text = "*", padx = 40, pady = 20, command = multiply)
num_divided = Button(root,text = "/", padx = 40, pady = 20, command = divided )
num_clear = Button(root,text = "C", padx = 40, pady = 20, command = clear_def )
num_equal = Button(root,text = "=", padx = 40, pady = 20, command = equal )
## grid command is for show number.

num_1.grid(row=1,column = 0)
num_2.grid(row=1,column = 1)
num_3.grid(row=1,column = 2)
num_add.grid(row=1,column = 3)

num_4.grid(row=2,column = 0)
num_5.grid(row=2,column = 1)
num_6.grid(row=2,column = 2)
num_minus.grid(row=2,column = 3)

num_7.grid(row=3,column = 0)
num_8.grid(row=3,column = 1)
num_9.grid(row=3,column = 2)
num_multiply.grid(row=3,column = 3)

num_0.grid(row=4,column = 0)
num_divided.grid(row=4,column = 1)
num_clear.grid(row=4,column = 2)
num_equal.grid(row=4,column = 3)

root.mainloop()