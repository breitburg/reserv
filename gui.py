'''
Этот скрипт отвечает за графический интерфейс
Создан в 2017 Батухтиным Ильёй.
Copyright © Upbits Team, 2018.
Требования: Любая система, Python 3, Tkinter library

Отредактирован Ketsu8, 14 февраля 2018. С днем всех влюбленных :)
'''

from tkinter import *  # Импорт tkinter'а
import tkinter.ttk as ttk  # Импорт ttk
from tkinter import filedialog  # Импорт из tkinter'а filedialog
from tkinter import messagebox  # Импорт из tkinter'а messagebox
from belfrywidgets import ToolTip  # Импорт из belfrywidgets ToolTip
import platform,threading  # Импорт platform,threading


class showWelcomeWindow():
    def show(self):
        self.root = Tk()
        windowX = int(self.root.winfo_screenwidth() / 2 - 325)  # Вычисление центра экрана пользователя по X'у
        windowY = int(self.root.winfo_screenheight() / 2 - 200)  # Вычисление центра экрана пользователя по Y'у
        self.root.title("Reserv")  # Сэтим имя окна
        self.root.geometry("650x400+" + str(windowX) + "+" + str(windowY))  # Сэтим размер окна
        self.root.resizable(False,False)  # Установка возможности изменить размер окна на False (По ширине и длине)
        self.root.protocol("WM_DELETE_WINDOW",quit)  # Установка зарезервированной функции quit на кнопку "X"

        s = ttk.Style()
        s.configure("TButton",bg="white",fg="black",font="arial 10")  # Создание стиля "TButton"

        welcomeLabel = Label(self.root,text="Добро пожаловать в Reserv",
                             font="arial 10")  # Создание текста со свойствами
        welcomeLabel.place(x=200,y=150,width=250,height=50)  # Размещение текста по кординатам и установка площади

        copyrightLabel = Label(self.root,text="Copyright © Upbits, 2017",
                               font="arial 10")  # Создание текста со свойствами
        copyrightLabel.place(x=200,y=350,width=250,height=50)  # Размещение текста по кординатам

        nextButton = ttk.Button(self.root,text="Начать",style="TButton",
                                command=self.destroyWindow)  # Создание кнопки со свойствами
        nextButton.place(x=275,y=190,width=100,height=28)  # Размещение кнопки по кординатам

        self.root.mainloop()

    def destroyWindow(self):
        self.root.destroy()  # Уничтожение окна


class showSettingsWindow():
    def show(self,name,port,onlineMode,CBE,PVP,D,GM):
        self.returnArray = []  # Создание массива returnArray
        self.root = Tk()
        windowX = int(self.root.winfo_screenwidth() / 2 - 325)  # Вычисление центра экрана пользователя по X'у
        windowY = int(self.root.winfo_screenheight() / 2 - 200)  # Вычисление центра экрана пользователя по Y'у
        self.root.title("Reserv")  # Сэтим имя окна
        self.root.geometry("650x400+" + str(windowX) + "+" + str(windowY))  # Сэтим размер окна
        self.root.resizable(False,False)  # Установка возможности изменить размер окна на False (По ширине и длине)
        self.root.protocol("WM_DELETE_WINDOW",self.appExit)  # Установка функции appExit на кнопку "X"

        s = ttk.Style()
        s.configure("TButton",bg="white",fg="black",font="arial 10")  # Создание стиля "TButton"
        s.configure("TEntry",font="arial 10")  # Создание стиля "TEntry"

        self.onlineMode_Choose = IntVar()
        self.onlineMode_Choose.set(1)

        self.CBE_Choose = IntVar()
        self.CBE_Choose.set(0)

        self.PVP_Choose = IntVar()
        self.PVP_Choose.set(1)

        name_Label = Label(self.root,text="Описание сервера:",font="arial 10")
        name_Label.place(x=0,y=0)
        ToolTip(name_Label,
                "Описание сервера, отображаемое при подключении в списке серверов. Поддерживает форматирование текста.")
        self.name_Entry = ttk.Entry(self.root,style="TEntry")
        self.name_Entry.place(x=120,y=0,width=190,height=20)
        ToolTip(self.name_Entry,
                "Описание сервера, отображаемое при подключении в списке серверов. Поддерживает форматирование текста.")

        port_Label = Label(self.root,text="Порт сервера:",font="arial 10")
        port_Label.place(x=0,y=40)
        ToolTip(port_Label,
                "Данный параметр определяет значение порта в протоколах TCP и UDP, который будет использовать сервер игры")
        self.port_Entry = ttk.Entry(self.root,style="TEntry")
        self.port_Entry.place(x=90,y=40,width=190,height=20)
        ToolTip(self.port_Entry,
                "Данный параметр определяет значение порта в протоколах TCP и UDP, который будет использовать сервер игры")

        MP_Label = Label(self.root,text="Максимальное количество игроков:",font="arial 10")
        MP_Label.place(x=0,y=80)
        self.MP_Entry = ttk.Entry(self.root,style="TEntry")
        self.MP_Entry.place(x=220,y=80,width=190,height=20)

        onlineMode_Check = ttk.Checkbutton(self.root,text="Онлайн режим",variable=self.onlineMode_Choose,onvalue=1,
                                           offvalue=0)
        onlineMode_Check.place(x=0,y=120)
        ToolTip(onlineMode_Check,
                "Этот параметр позволяет включить/выключить проверку подлинности премиум-аккаунтов пользователей, которые подключаются к данному серверу.")

        CBE_Check = ttk.Checkbutton(self.root,text="Командный блок",variable=self.CBE_Choose,onvalue=1,offvalue=0)
        CBE_Check.place(x=0,y=160)
        ToolTip(CBE_Check,
                "Позволяет использовать командный блок. Эта опция не генерируется при первой загрузке, а появляется при первой попытке использования командного блока.")

        PVP_Check = ttk.Checkbutton(self.root,text="PVP",variable=self.PVP_Choose,onvalue=1,offvalue=0)
        PVP_Check.place(x=0,y=200)
        ToolTip(PVP_Check,
                "Включает/отключает получение урона игрокам от атак других игроков на сервере. При true игроки смогут «воевать» между собой, убивая друг друга. Если уставлено значение false, игроки не смогут наносить прямой урон один другому.")

        D_Label = Label(self.root,text="Сложность:",font="arial 10")
        D_Label.place(x=0,y=240)
        ToolTip(D_Label,"Уровень сложности")
        self.D_Combo = ttk.Combobox(self.root,values=["Мирная","Лёгкая","Нормальная","Сложная"],height=4,
                                    state="readonly")
        self.D_Combo.place(x=72,y=240)
        self.D_Combo.set("Нормальная")
        self.D_Combo.bind("<FocusIn>",self.antiSelection)
        ToolTip(self.D_Combo,"Уровень сложности")

        GM_Label = Label(self.root,text="Режим игры:",font="arial 10")
        GM_Label.place(x=0,y=280)
        ToolTip(GM_Label,"Игровой режим по умолчанию")
        self.GM_Combo = ttk.Combobox(self.root,values=["Выживание","Креатив","Приключение","Наблюдатель"],height=4,
                                     state="readonly")
        self.GM_Combo.place(x=80,y=280)
        self.GM_Combo.set("Выживание")
        self.GM_Combo.bind("<FocusIn>",self.antiSelection)
        ToolTip(self.GM_Combo,"Игровой режим по умолчанию")

        nextButton = ttk.Button(self.root,text="Далее",style="TButton",
                                command=self.nextAction)  # Создание кнопки со свойствами
        nextButton.place(x=485,y=370,width=100,height=25)  # Размещение кнопки по кординатам и установка площади

        backButton = ttk.Button(self.root,text="Назад",style="TButton",command=self.backAction,
                                state=DISABLED)  # Создание кнопки со свойствами
        backButton.place(x=370,y=370,width=100,height=25)  # Размещение кнопки по кординатам и установка площади

        if name is not None:
            self.name_Entry.insert(1.0,name)

        if port is not None:
            self.port_Entry.insert(1.0,port)

        if onlineMode is not None:
            self.onlineMode_Choose.set(onlineMode)

        if CBE is not None:
            self.CBE_Choose.set(CBE)

        if PVP is not None:
            self.PVP_Choose.set(PVP)

        if D is not None:
            self.D_Combo.set(D)

        if GM is not None:
            self.GM_Choose.set(GM)

        self.root.mainloop()
        return self.returnArray

    def antiSelection(self,event):
        event.widget.master.focus_set()

    def nextAction(self):
        self.returnArray = ["NEXT",self.name_Entry.get(),self.port_Entry.get(),self.onlineMode_Choose.get(),
                            self.CBE_Choose.get(),self.PVP_Choose.get(),self.MP_Entry.get(),self.D_Combo.get(),
                            self.GM_Combo.get()]
        self.root.destroy()  # Уничтожение окна

    def backAction(self):
        self.returnArray = ["BACK",self.name_Entry.get(),self.port_Entry.get(),self.D_Combo.get(),self.GM_Combo.get(),
                            self.CBE_Choose.get(),self.PVP_Choose.get()]
        self.root.destroy()  # Уничтожение окна

    def appExit(self):
        if messagebox.askokcancel("Выйти?",
                                  "Вы точно хотите выйти из программы?"):  # Если результат ответа от пользователя положительный
            quit()  # то выполняется зарезервированная функция quit


class showVersionWindow():
    def show(self,VersionArray,Version):
        self.returnArray = []  # Создание массива returnArray
        self.root = Tk()
        windowX = int(self.root.winfo_screenwidth() / 2 - 325)  # Вычисление центра экрана пользователя по X'у
        windowY = int(self.root.winfo_screenheight() / 2 - 200)  # Вычисление центра экрана пользователя по Y'у
        self.root.title("Reserv")  # Сэтим имя окна
        self.root.geometry("650x400+" + str(windowX) + "+" + str(windowY))  # Сэтим размер окна
        self.root.resizable(False,False)  # Установка возможности изменить размер окна на False (По ширине и длине)
        self.root.protocol("WM_DELETE_WINDOW",self.appExit)  # Установка функции appExit на кнопку "X"

        s = ttk.Style()
        s.configure("TButton",bg="white",fg="black",font="arial 10")  # Создание стиля "TButton"

        informationLabel = Label(text="Выберите версию сервера:",font="arial 10")  # Создание текста со свойствами
        informationLabel.place(x=0,y=0)  # Размещение текста по кординатам и установка площади

        self.serverChoose = IntVar()
        self.serverChoose.set(
            1)  # Установка значения serverChoose 1. P.S. Обычная переменная почему-то не работает. Это решение я нашёл на форуме. Почему не работает я разбираться не стал
        ycord = 0
        mode = 0

        canvas = Canvas(self.root)  # Создание холста со свойствами
        versionScroll = Scrollbar(self.root,orient='vertical',
                                  command=canvas.yview)  # Создание scrollbar'а со свойствами

        for text in VersionArray:  # Перебор массива VersionArray который поставляется из main.py
            mode = int(mode) + 1  # + 1 к mode
            serverButton = ttk.Radiobutton(self.root,text=text,variable=self.serverChoose,
                                           value=mode)  # Создание переключателя со свойствами
            canvas.create_window(0,ycord,anchor='nw',window=serverButton,
                                 height=0)  # Установка переключателя внутрь холста
            ycord = ycord + 25  # + 25 к ycord

        canvas.configure(scrollregion=canvas.bbox('all'),yscrollcommand=versionScroll.set)  # Изменение свойств холста
        canvas.place(x=0,y=45,height=300)  # Размещение холста по кординатам и установка площади
        versionScroll.place(x=635,y=0,width=15,height=400)  # Размещение scrollbar'а по кординатам и установка площади

        nextButton = ttk.Button(self.root,text="Далее",style="TButton",
                                command=self.nextAction)  # Создание кнопки со свойствами
        nextButton.place(x=485,y=370,width=100,height=25)  # Размещение кнопки по кординатам и установка площади

        backButton = ttk.Button(self.root,text="Назад",style="TButton",command=self.backAction,
                                state=DISABLED)  # Создание кнопки со свойствами
        backButton.place(x=370,y=370,width=100,height=25)  # Размещение кнопки по кординатам и установка площади

        if Version is not None:
            self.serverChoose.set(Version)

        self.root.mainloop()
        return self.returnArray

    def nextAction(self):
        self.returnArray.insert(0,"NEXT")  # Установка значения NEXT в 0 индекс массива
        self.returnArray.insert(1,
                                self.serverChoose.get())  # Установка значения переменной serverChoose в 1 индекс массива через функцию get()
        self.root.destroy()  # Уничтожение окна
        pass

    def backAction(self):
        self.returnArray.insert(0,"BACK")  # Установка значения BACK в 0 индекс массива
        self.returnArray.insert(1,
                                self.serverChoose.get())  # Установка значения переменной serverChoose в 1 индекс массива через функцию get()
        self.root.destroy()  # Уничтожение окна

    def appExit(self):
        if messagebox.askokcancel("Предупреждение",
                                  "Вы точно хотите выйти из программы?"):  # Если результат ответа от пользователя положительный
            quit()  # то выполняется зарезервированная функция quit


class showServerInfoWindow():
    def show(self,name,port,onlineMode,CBE,PVP,D,GM):
        self.returnArray = []  # Создание массива returnArray
        self.root = Tk()
        windowX = int(self.root.winfo_screenwidth() / 2 - 325)  # Вычисление центра экрана пользователя по X'у
        windowY = int(self.root.winfo_screenheight() / 2 - 200)  # Вычисление центра экрана пользователя по Y'у
        self.root.title("Reserv")  # Сэтим имя окна
        self.root.geometry("650x400+" + str(windowX) + "+" + str(windowY))  # Сэтим размер окна
        self.root.resizable(False,False)  # Установка возможности изменить размер окна на False (По ширине и длине)
        self.root.protocol("WM_DELETE_WINDOW",self.appExit)  # Установка функции appExit на кнопку "X"

        s = ttk.Style()
        s.configure("TButton",bg="white",fg="black",font="arial 10")  # Создание стиля "TButton"
        s.configure("TEntry",font="arial 10")  # Создание стиля "TEntry"

        serverNameLabel = Label(self.root,text="Имя сервера: " + name)
        serverNameLabel.place(x=0,y=0)

        portNameLabel = Label(self.root,text="Порт сервера: " + port)
        portNameLabel.place(x=0,y=25)

        onlineModeLabel = Label(self.root,text="Онлайн режим: " + onlineMode)
        onlineModeLabel.place(x=0,y=50)

        CBELabel = Label(self.root,text="Командный блок: " + CBE)
        CBELabel.place(x=0,y=75)

        PVPLabel = Label(self.root,text="PVP: " + PVP)
        PVPLabel.place(x=0,y=100)

        DLabel = Label(self.root,text="Сложность: " + D)
        DLabel.place(x=0,y=125)

        GMLabel = Label(self.root,text="Игровой режим: " + GM)
        GMLabel.place(x=0,y=150)

        nextButton = ttk.Button(self.root,text="собрать!",style="TButton",
                                command=self.nextAction)  # Создание кнопки со свойствами
        nextButton.place(x=485,y=370,width=100,height=25)  # Размещение кнопки по кординатам и установка площади

        backButton = ttk.Button(self.root,text="отменить",style="TButton",
                                command=self.backAction)  # Создание кнопки со свойствами
        backButton.place(x=370,y=370,width=100,height=25)  # Размещение кнопки по кординатам и установка площади

        self.root.mainloop()
        return

    def nextAction(self):
        self.root.destroy()

    def backAction(self):
        quit(0)

    def appExit(self):
        if messagebox.askokcancel("Предупреждение",
                                  "Вы точно хотите выйти из программы?"):  # Если результат ответа от пользователя положительный
            quit()  # то выполняется зарезервированная функция quit


class showCreateWindow():
    def show(self,event,serverName):
        self.returnArray = []  # Создание массива returnArray
        self.root = Tk()
        windowX = int(self.root.winfo_screenwidth() / 2 - 325)  # Вычисление центра экрана пользователя по X'у
        windowY = int(self.root.winfo_screenheight() / 2 - 200)  # Вычисление центра экрана пользователя по Y'у
        self.root.title("Reserv")  # Сэтим имя окна
        self.root.geometry("450x100+" + str(windowX) + "+" + str(windowY))  # Сэтим размер окна
        self.root.resizable(False,False)  # Установка возможности изменить размер окна на False (По ширине и длине)
        self.root.protocol("WM_DELETE_WINDOW",self.ingore)  # Установка функции appExit на кнопку "X"

        self.serverNameLabel = Label(self.root,text="Сборка сервера " + serverName + "...")
        self.serverNameLabel.place(x=0,y=0)

        self.infoCreateLabel = Label(self.root,text="")
        self.infoCreateLabel.place(x=180,y=40)

        event.set()
        self.root.mainloop()
        return self.returnArray

    def exit(self):
        self.root.destroy()

    def end(self):
        self.infoCreateLabel.destroy()
        self.serverNameLabel.destroy()
        nextButton = ttk.Button(self.root,text="Готово",style="TButton",
                                command=self.nextAction)  # Создание кнопки со свойствами
        nextButton.place(x=180,y=40,width=100,height=25)  # Размещение кнопки по кординатам и установка площади

    def ingore(self):
        pass

    def changeText(self,textV):
        self.infoCreateLabel.configure(text=textV)

    def nextAction(self):
        quit(0)

    def backAction(self):
        quit(0)


class showPluginWindow():
    def show(self,PluginsArray):
        self.returnArray = []
        self.root = Tk()
        windowX = int(self.root.winfo_screenwidth() / 2 - 325)
        windowY = int(self.root.winfo_screenheight() / 2 - 200)
        self.root.title("Reserv")
        self.root.geometry("650x400+" + str(windowX) + "+" + str(windowY))
        self.root.resizable(False,False)
        self.root.protocol("WM_DELETE_WINDOW",self.appExit)

        s = ttk.Style()
        s.configure("TButton",bg="white",fg="black",font="arial 10")

        informationLabel = Label(text="Выберите плагины:",font="arial 10")
        informationLabel.place(x=0,y=0)

        ycord = 0

        self.checkButtonsDict = {}

        canvas = Canvas(self.root)
        versionScroll = Scrollbar(self.root,orient='vertical',command=canvas.yview)
        for text in PluginsArray:
            checkValue = BooleanVar()
            pluginButton = ttk.Checkbutton(self.root,text=text,variable=checkValue)
            canvas.create_window(0,ycord,anchor='nw',window=pluginButton,
                                 height=0)

            self.checkButtonsDict[text] = checkValue

            ycord = ycord + 25

        canvas.configure(scrollregion=canvas.bbox('all'),yscrollcommand=versionScroll.set)
        canvas.place(x=0,y=45,height=300)
        versionScroll.place(x=635,y=0,width=15,height=400)

        nextButton = ttk.Button(self.root,text="Далее",style="TButton",
                                command=self.nextAction)
        nextButton.place(x=485,y=370,width=100,height=25)

        backButton = ttk.Button(self.root,text="Назад",style="TButton",command=self.backAction,
                                state=DISABLED)  # Создание кнопки со свойствами
        backButton.place(x=370,y=370,width=100,height=25)  # Размещение кнопки по кординатам и установка площади

        self.root.mainloop()
        return self.checkButtonsDict

    def nextAction(self):
        self.returnArray.insert(0,"NEXT")  # Установка значения NEXT в 0 индекс массива
        self.returnArray.insert(1,self.checkButtonsDict)
        self.root.destroy()  # Уничтожение окна
        pass

    def backAction(self):
        self.returnArray.insert(0,"BACK")  # Установка значения BACK в 0 индекс массива
        self.returnArray.insert(1,
                                self.checkButtonsDict)
        self.root.destroy()  # Уничтожение окна

    def appExit(self):
        if messagebox.askokcancel("Предупреждение",
                                  "Вы точно хотите выйти из программы?"):  # Если результат ответа от пользователя положительный
            quit()  # то выполняется зарезервированная функция quit
