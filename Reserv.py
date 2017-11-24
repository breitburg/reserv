
from tkinter import *

root = Tk()
root.title("Reserv")
root.geometry("650x400+0+0")
root.resizable(False, False)
root.iconbitmap("resources/icon.ico")

label_welcome = Label(root,text="Добро пожаловать в Reserv")
label_welcome.place(x=225,y=350,width=200,height=350)

label_copyright = Label(root,text="Copyright © 2017")
label_copyright.place(x=225,y=150,width=200,height=350)

button_1 = Button(root,text="Начать",bg="white",fg="black",font="arial")
button_1.place(x=275,y=190,width=100,height=35)

root.mainloop()
