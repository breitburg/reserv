
from tkinter import *

root = Tk()
root.title("Reserv")
root.geometry("650x400+0+0")
root.resizable(False, False)
root.iconbitmap("resources/icon.ico")
button_1 = Button(root,text="1",bg="white",fg="black",font="arial 20")
button_1.place(x=225,y=150,width=200,height=50)

root.mainloop()
