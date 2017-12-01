'''
Этот скрипт отвечает за графический интерфейс
Создан в 2017 Батухтиным Ильёй.
Copyright © Upbits Team, 2017.
Требования: Любая система, Python 3, Tkinter library
'''
from tkinter import * #Импорт tkinter'а
from tkinter import filedialog #Импорт из tkinter'а filedialog
from tkinter import messagebox #Импорт из tkinter'а messagebox

class showWelcomeWindow():
    def show(self):
        self.root = Tk()
        windowX = int(self.root.winfo_screenwidth() / 2 - 325) #Вычисление центра экрана пользователя по X'у
        windowY = int(self.root.winfo_screenheight() / 2 - 200) #Вычисление центра экрана пользователя по Y'у
        self.root.title("Reserv") #Сэтим имя окна
        self.root.geometry("650x400+" + str(windowX) + "+" + str(windowY)) #Сэтим размер окна
        self.root.resizable(False, False) #Установка возможности изменить размер окна на False (По ширине и длине)
        self.root.protocol("WM_DELETE_WINDOW", quit) #Установка зарезервированной функции quit на кнопку "X" 

        welcomeLabel = Label(self.root,text="Добро пожаловать в Reserv",font="arial 10") #Создание текста со свойствами
        welcomeLabel.place(x=200,y=150,width=250,height=50) #Размещение текста по кординатам и установка площади

        copyrightLabel = Label(self.root,text="Copyright © Upbits Team, 2017",font="arial 10") #Создание текста со свойствами
        copyrightLabel.place(x=200,y=350,width=250,height=50) #Размещение текста по кординатам

        nextButton = Button(self.root,text="Начать",bg="white",fg="black",font="arial 10",command=self.destroyWindow) #Создание кнопки со свойствами
        nextButton.place(x=275,y=190,width=100,height=28) #Размещение кнопки по кординатам

        self.root.mainloop()
        pass

    def destroyWindow(self):
        self.root.destroy() #Уничтожение окна
        pass
    pass

class showPathWindow():
    def show(self):
        self.root = Tk()
        windowX = int(self.root.winfo_screenwidth() / 2 - 325) #Вычисление центра экрана пользователя по X'у
        windowY = int(self.root.winfo_screenheight() / 2 - 200) #Вычисление центра экрана пользователя по Y'у
        self.root.title("Reserv") #Сэтим имя окна
        self.root.geometry("650x400+" + str(windowX) + "+" + str(windowY)) #Сэтим размер окна
        self.root.resizable(False, False) #Установка возможности изменить размер окна на False (По ширине и длине)
        self.root.protocol("WM_DELETE_WINDOW", self.appExit) #Установка функции appExit на кнопку "X"

        informationLabel = Label(self.root,text="Выберите директорию сервера",font="arial 10") #Cоздание текста со свойствами
        informationLabel.place(x=225,y=160,width=200,height=20) #Размещение текста по кординатам и установка площади

        self.directoryEntry = Entry(self.root,font="arial 10") #Cоздание поля со свойствами
        self.directoryEntry.place(x=225,y=200,width=200,height=20) #Размещение поля по кординатам и установка площади

        dialogButton = Button(self.root,text="...",font="arial 10",command=self.showFileDialog) #Создание кнопки со свойствами
        dialogButton.place(x=425,y=200,width=20,height=20) #Размещение кнопки по кординатам и установка площади

        nextButton = Button(text="далее",font="arial 10",command=self.nextAction) #Создание кнопки со свойствами
        nextButton.place(x=485,y=370,width=100,height=25) #Размещение кнопки по кординатам и установка площади

        self.root.mainloop()
        pass
    
    def showFileDialog(self):
        self.root.filename = filedialog.askdirectory() #Создание диалога выбора папки и запись результата в переменную
        self.directoryEntry.delete('0', END) #Удаление текста из directoryEntry
        self.directoryEntry.insert(1, self.root.filename) #Добавление результата работы диалога папки в directoryEntry
        pass

    def nextAction(self):
        self.root.destroy() #Уничтожение окна
        pass
    
    def appExit(self):
        if messagebox.askokcancel("Выйти?","Вы точно хотите выйти из программы?"): #Если результат ответа от пользователя положительный
            quit() #то выполняется зарезервированная функция quit
            pass
        pass

class showVersionWindow():
    def show(self,VersionArray):
        self.returnArray = [] #Создание массива returnArray
        self.root = Tk()
        windowX = int(self.root.winfo_screenwidth() / 2 - 325) #Вычисление центра экрана пользователя по X'у
        windowY = int(self.root.winfo_screenheight() / 2 - 200) #Вычисление центра экрана пользователя по Y'у
        self.root.title("Reserv") #Сэтим имя окна 
        self.root.geometry("650x400+" + str(windowX) + "+" + str(windowY)) #Сэтим размер окна
        self.root.resizable(False, False) #Установка возможности изменить размер окна на False (По ширине и длине)
        self.root.protocol("WM_DELETE_WINDOW", self.appExit) #Установка функции appExit на кнопку "X"

        informationLabel = Label(text="Выберите версию сервера:",font="arial 10") #Создание текста со свойствами
        informationLabel.place(x=0,y=0) #Размещение текста по кординатам и установка площади

        self.serverChoose = IntVar()
        self.serverChoose.set(1) #Установка значения serverChoose 1. P.S. Обычная переменная почему-то не работает. Это решение я нашёл на форуме. Почему не работает я разбираться не стал
        ycord = 0
        mode = 0

        canvas = Canvas(self.root) #Создание холста со свойствами
        versionScroll = Scrollbar(self.root,orient='vertical',command=canvas.yview) #Создание scrollbar'а со свойствами

        for text in VersionArray: #Перебор массива VersionArray который поставляется из main.py
            mode = int(mode) + 1 # + 1 к mode
            serverButton = Radiobutton(self.root, text=text,variable=self.serverChoose, value=mode) #Создание переключателя со свойствами
            canvas.create_window(0, ycord, anchor='nw', window=serverButton, height=0) #Установка переключателя внутрь холста
            ycord = ycord + 25 # + 25 к ycord
            pass

        canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=versionScroll.set) #Изменение свойств холста
        canvas.place(x=0,y=45,height=300) #Размещение холста по кординатам и установка площади
        versionScroll.place(x=635,y=0,width=15,height=400) #Размещение scrollbar'а по кординатам и установка площади 

        button_next = Button(self.root,text="далее",command=self.nextAction) #Создание кнопки со свойствами
        button_next.place(x=485,y=370,width=100,height=25) #Размещение кнопки по кординатам и установка площади

        button_back = Button(self.root,text="назад",command=self.backAction) #Создание кнопки со свойствами
        button_back.place(x=370,y=370,width=100,height=25) #Размещение кнопки по кординатам и установка площади

        self.root.mainloop()
        return self.returnArray
    
    def nextAction(self):
        self.root.destroy() #Уничтожение окна
        self.returnArray.insert(0,"NEXT") #Установка значения NEXT в 0 индекс массива
        self.returnArray.insert(1,self.serverChoose.get()) #Установка значения переменной serverChoose в 1 индекс массива через функцию get()
        pass
    
    def backAction(self):
        self.root.destroy() #Уничтожение окна
        self.returnArray.insert(0,"BACK") #Установка значения BACK в 0 индекс массива
        self.returnArray.insert(1,self.serverChoose.get()) #Установка значения переменной serverChoose в 1 индекс массива через функцию get()
        pass
    
    def appExit(self):
        if messagebox.askokcancel("Выйти?","Вы точно хотите выйти из программы?"): #Если результат ответа от пользователя положительный
            quit() #то выполняется зарезервированная функция quit
            pass
        pass

#НЕДОДЕЛАНО, НЕ ИСПОЛЬЗОВАТЬ!!!!

def showSettingsWindow():
    root = Tk()
    windowX = int(root.winfo_screenwidth() / 2 - 325)
    windowY = int(root.winfo_screenheight() / 2 - 200)
    root.title("Reserv") #Сэтим имя окна 
    root.geometry("650x400+" + str(windowX) + "+" + str(windowY)) #Сэтим размер окна
    root.resizable(False, False) #Установка возможности изменить размер окна на False (По ширине и длине)
    pass