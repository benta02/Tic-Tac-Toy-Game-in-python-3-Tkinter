from tkinter import *
from tkinter import Tk
from tkinter import ttk
from tkinter import  messagebox

window = Tk()

window.title("tic tac toy")
s = ttk.Style()
s.theme_use('classic')

id1 = ""
id2 = ""
id3 = ""
id4 = ""
id5 = ""
id6 = ""
id7 = ""
id8 = ""
id9 = ""




btn1 = Button(window,text="", padx=50, pady=40,bg='#444',command=lambda : active(1))
btn2 = Button(window,text="", padx=50, pady=40,bg='#444',command=lambda : active(2))
btn3 = Button(window,text="", padx=50, pady=40,bg='#444',command=lambda : active(3))
btn4 = Button(window,text="", padx=50, pady=40,bg='#444',command=lambda : active(4))
btn5 = Button(window,text="", padx=50, pady=40,bg='#444',command=lambda : active(5))
btn6 = Button(window,text="", padx=50, pady=40,bg='#444',command=lambda : active(6))
btn7 = Button(window,text="", padx=50, pady=40,bg='#444',command=lambda : active(7))
btn8 = Button(window,text="", padx=50, pady=40,bg='#444',command=lambda : active(8))
btn9 = Button(window,text="", padx=50, pady=40,bg='#444',command=lambda : active(9))



btn1.grid(row=1 , column=1)
btn2.grid(row=1 , column=2)
btn3.grid(row=1 , column=3)

btn4.grid(row=2 , column=1)
btn5.grid(row=2 , column=2)
btn6.grid(row=2 , column=3)

btn7.grid(row=3 , column=1)
btn8.grid(row=3 , column=2)
btn9.grid(row=3 , column=3)

player = 1
def active(id):
    global player
    global id1
    global id2
    global id3
    global id4
    global id5
    global id6
    global id7
    global id8
    global id9
    if id ==1 and player==1:
        btn1.config(text="o",foreground="red",font= 77, bg="green")
        player = 2
        id1 = "o"
    elif id ==1 and player==2:
        btn1.config(text="x",foreground="green",font= 77, bg="yellow")
        player=1
        id1 ="x"

    elif id == 2 and player == 1 :
        btn2.config( text="o",foreground="red",font= 77, bg="green" )
        player = 2
        id2 = "o"
    elif id == 2 and player == 2 :
        btn2.config( text="x",foreground="green",font= 77 , bg="yellow")
        player = 1
        id2 = "x"


    elif id == 3 and player == 1 :
        btn3.config( text="o" ,foreground="red",font= 77, bg="green")
        player = 2
        id2 = "o"
    elif id == 3 and player == 2 :
        btn3.config( text="x",foreground="green",font= 77, bg="yellow" )
        player = 1
        id3 = "x"

    elif id == 4 and player == 1 :
        btn4.config( text="o" ,foreground="red",font= 77, bg="green")
        player = 2
        id4 = "o"
    elif id == 4 and player == 2 :
        btn4.config( text="x",foreground="green",font= 77 , bg="yellow")
        player = 1
        id4 = "x"


    elif id == 5 and player == 1 :
        btn5.config( text="o",foreground="red",font= 77 , bg="green")
        player = 2
        id5 = "o"
    elif id == 5 and player == 2 :
        btn5.config( text="x" ,foreground="green",font= 77, bg="yellow")
        player = 1
        id5 = "x"

    elif id == 6 and player == 1 :
        btn6.config( text="o",foreground="red" ,font= 77, bg="green")
        player = 2
        id6 = "o"
    elif id == 6 and player == 2 :
        btn6.config( text="x",foreground="green",font= 77 , bg="yellow")
        player = 1
        id6= "x"

    elif id == 7 and player == 1 :
        btn7.config( text="o" ,foreground="red",font= 77, bg="green")
        player = 2
        id7 = "o"
    elif id == 7 and player == 2 :
        btn7.config( text="x" ,foreground="green",font= 77, bg="yellow")
        player = 1
        id7 = "x"

    elif id == 8 and player == 1 :
        btn8.config( text="o" ,foreground="red",font= 77, bg="green")
        player = 2
        id8 = "o"
    elif id == 8 and player == 2 :
        btn8.config( text="x",foreground="green",font= 77 , bg="yellow")
        player = 1
        id8 = "x"

    elif id == 9 and player == 1 :
        btn9.config( text="o",foreground="red" ,font= 77, bg="green")
        player = 2
        id9 = "o"
    elif id == 9 and player == 2 :
        btn9.config( text="x" ,foreground="green",font= 77, bg="yellow")
        player = 1
        id9 = "x"

    if id1 == id2 ==id3 == "o" or id3 == id5 == id7=="o" or id1==id4==id7=="o" or id4 == id5 ==id6=="o" or id7 == id8 ==id9== "o" or id2 == id5 ==id8=="o" or id3 == id6 == id9 =="o":
        player = "o"
        messagebox.showinfo(message="Game end," + player + " is winer")

    if id1 == id2 ==id3 == "x" or id3 == id5 == id7=="x" or id1==id4==id7=="x" or id4 == id5 ==id6=="x" or id7 == id8 ==id9== "x" or id2 == id5 ==id8=="x" or id3 == id6 == id9 =="x":
        player = "x"
        messagebox.showinfo(message="Game end," + player + " is winer")

window.mainloop()

































