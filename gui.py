'''
Этот скрипт отвечает за графический интерфейс

Создан в 2017 Батухтиным Ильёй.
Copyright © Upbits Team, 2017.

Требования: Любая система, Python 3
'''
from tkinter import *
def showWelcomeScreen():
    root = Tk()
    root.title("Reserv") #Сэтим имя окна 
    root.geometry("650x400+0+0") #Сэтим размер окна
    root.resizable(False, False) #Установка возможности изменить размер окна на False (По ширине и длине)

    label_welcome = Label(root,text="Добро пожаловать в Reserv",font="arial 10") 
    label_welcome.place(x=200,y=150,width=250,height=50) #Размещение текста по кординатам

    label_copyright = Label(root,text="Copyright © Upbits Team, 2017",font="arial 10")
    label_copyright.place(x=200,y=350,width=250,height=50) #Размещение текста по кординатам

    button_next = Button(root,text="Начать",bg="white",fg="black",font="arial 10")
    button_next.place(x=275,y=190,width=100,height=28) #Размещение кнопки по кординатам
    root.mainloop()
    pass

