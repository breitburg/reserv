'''
Этот скрипт отвечает за графический интерфейс
Создан в 2017 Батухтиным Ильёй.
Copyright © Upbits Team, 2017.
Требования: Любая система, Python 3, Tkinter library
'''
from tkinter import *
def showWelcomeWindow():
    root = Tk()
    windowX = int(root.winfo_screenwidth() / 2 - 325)
    windowY = int(root.winfo_screenheight() / 2 - 200)
    root.title("Reserv") #Сэтим имя окна 
    root.geometry("650x400+" + str(windowX) + "+" + str(windowY)) #Сэтим размер окна
    root.resizable(False, False) #Установка возможности изменить размер окна на False (По ширине и длине)

    label_welcome = Label(root,text="Добро пожаловать в Reserv",font="arial 10") #Создание теста со свойствами
    label_welcome.place(x=200,y=150,width=250,height=50) #Размещение текста по кординатам

    label_copyright = Label(root,text="Copyright © Upbits Team, 2017",font="arial 10") #Создание теста со свойствами
    label_copyright.place(x=200,y=350,width=250,height=50) #Размещение текста по кординатам

    button_next = Button(root,text="Начать",bg="white",fg="black",font="arial 10",command=root.destroy) #Создание кнопки со свойствами
    button_next.place(x=275,y=190,width=100,height=28) #Размещение кнопки по кординатам
    root.mainloop()
    pass

def showVersionWindow(VersionArray):
    root = Tk()
    windowX = int(root.winfo_screenwidth() / 2 - 325)
    windowY = int(root.winfo_screenheight() / 2 - 200)
    root.title("Reserv") #Сэтим имя окна 
    root.geometry("650x400+" + str(windowX) + "+" + str(windowY)) #Сэтим размер окна
    root.resizable(False, False) #Установка возможности изменить размер окна на False (По ширине и длине)

    informationLabel = Label(text="Выберите версию сервера:",font="arial 10")
    informationLabel.place(x=0,y=0)

    serverChoose = IntVar() 
    serverChoose.set(1)  
    ycord = 0
    mode = 0

    canvas = Canvas(root)
    versionScroll = Scrollbar(root,orient='vertical',command=canvas.yview)

    for text in VersionArray:
        mode = int(mode) + 1
        serverButton = Radiobutton(root, text=text,variable=serverChoose, value=mode)
        canvas.create_window(0, ycord, anchor='nw', window=serverButton, height=0)
        ycord = ycord + 25
        pass

    canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=versionScroll.set)
    canvas.place(x=0,y=45,height=300)
    versionScroll.place(x=635,y=0,width=15,height=400)

    button_next = Button(root,text="далее",bg="gray")
    button_next.place(x=485,y=370,width=150,height=30)
    button_back = Button(root,text="назад",bg="gray")
    button_back.place(x=335,y=370,width=150,height=30)
    root.mainloop()
    return serverChoose.get()

def showSettingsWindow():
    root = Tk()
    windowX = int(root.winfo_screenwidth() / 2 - 325)
    windowY = int(root.winfo_screenheight() / 2 - 200)
    root.title("Reserv") #Сэтим имя окна 
    root.geometry("650x400+" + str(windowX) + "+" + str(windowY)) #Сэтим размер окна
    root.resizable(False, False) #Установка возможности изменить размер окна на False (По ширине и длине)
    pass
