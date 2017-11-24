
from tkinter import *

root = Tk()
root.title("Reserv")
root.geometry("650x400+0+0")
root.resizable(False, False)
root.iconbitmap("resources/icon.ico")

label_welcome = Label(root,text="Добро пожаловать в Reserv",font="arial")
label_welcome.place(x=200,y=150,width=250,height=50)

label_copyright = Label(root,text="Copyright © 2017",font="arial")
label_copyright.place(x=200,y=350,width=250,height=50)

button_1 = Button(root,text="Начать",bg="white",fg="black",font="arial")
button_1.place(x=275,y=190,width=100,height=35)

root.mainloop()
