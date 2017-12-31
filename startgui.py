'''
Reserv GUI

Copyright © Upbits Team, 2017 – 2018.
GitHub: http://github.com/Upbits/

По вопросом Reserv писать сюда:
https://vk.com/upbits или на почту
<upbits@blinkhub.ru>.

Удачного использования :D
'''
try:
    import os, zipfile, wget, essentials, platform, time, requests, gui, belfrywidgets, threading, sys #импорт всех нужных библиотек
except:
    import platform, os
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    print("У вас не найдены некоторые библиотеки которые нужны для работы программы, либо при импорте библиотек произошла ошибка. Сейчас произайдет автоматическая установка нужных библиотек.")
    if platform.system() == "Windows":
        os.system("pip3 install wget requests")
    else:
        os.system("sudo pip3 install wget requests")
    print("Все библиотеки установлены. Сейчас произайдет перезапуск Reserv.")
    time.sleep(3)
    os.system("python3 lite.py")

 #вызов функции универсальной отчистки
welcome = gui.showWelcomeWindow()
welcome.show()


#приветствие и ввод адреса сервера
config = gui.showSettingsWindow()
s = config.show(None, None, None, None, None, None, None)
serverName = s[1]
serverPort = s[2]

if serverName == "":
    serverName = "Reserv Server"

if serverPort == "":
    serverPort = "25565"

#диалоговое окно в терминале кароч
#выбор online-mode на true или false
serverMode = s[3]

#максимальное колличество игроков
serverMaxPlayers = s[6]
if serverMaxPlayers == "":
    serverMaxPlayers = "20"

#доступны ли командные блоки на сервере
serverCBE = s[4]

#доступно ли PVP
serverPVP = s[5]

serverDiff = s[7]

gameMode = s[8]

#ядро сервера
ver = gui.showVersionWindow()
verList = ["1.12", "1.11", "1.10", "1.9", "1.8", "1.5"]
choosedVersion = ver.show(verList, None)
serverCore = str(verList[int(choosedVersion[1]) - 1])

#начинается полный пипец
info = gui.showServerInfoWindow()
if serverMode == 1:
    serverMode = "да"
else:
    serverMode = "нет"
if serverCBE == 1:
    serverCBE = "да"
else:
    serverCBE = "нет"
if serverPVP == 1:
    serverPVP = "да"
else:
    serverPVP = "нет"

info.show(serverName, serverPort, str(serverMode), str(serverCBE), str(serverPVP), serverDiff, gameMode)

controlEvent = threading.Event()
creatingWindow = gui.showCreateWindow()

def windowThread():
    creatingWindow.show(controlEvent,serverName)

t = threading.Thread(target=windowThread)
t.start()

controlEvent.wait()

creatingWindow.changeText("Загрузка сервера...")
#скачивается база сервера с сервера
#прямо рекурсия получается
wget.download("http://hack.blinkhub.ru/reserv/guiserv.zip", "server.zip")
creatingWindow.changeText("Распаковка сервера...")
#распаковывается сервер
#используя функцию unZip из
#нашей библиотеки Essentials
essentials.unZip("server.zip", "server/")
os.remove("server.zip")
creatingWindow.changeText("Загрузка ядра....")
#дальше идет загрузка самого важного компанента
#сервера – ядра... короче просто подставляется 
#переменная с версией ядра... все очень просто
#и с костылями конечго-же... потом как-нибуть...
wget.download("http://hack.blinkhub.ru/reserv/cores/" + serverCore + ".jar", "server/")
creatingWindow.changeText("\nНастройка параметров...")
#уу! настройка параметров!
#готовится самая главная переменная
#в которую записан весь текст из файла
#конфигурации сервера Minecraft
servProperties = essentials.textFromFile("server/server.properties") #вот она это строчка судьбы
#дальше идет намализация переменных
#которче, готовится к тому что-бы быть
#записанным в файл конфига
if serverDiff == "Мирная":
    serverDiff = "0"
elif serverDiff == "Легкая":
    serverDiff = "1"
elif serverDiff == "Нормальная":
    serverDiff = "2"
elif serverDiff == "Сложная":
    serverDiff = "3"

if gameMode == "Выживание":
    gameMode = "0"
elif gameMode == "Креатив":
    gameMode = "1"
elif gameMode == "Приключение":
    gameMode = "2"
elif gameMode == "Наблюдатель":
    gameMode = "3"

if serverMode == "да":
    serverMode = "true"
else:
    serverMode = "false"

if serverCBE == "да":
    serverCBE = "true"
else:
    serverCBE = "false"

if serverPVP == "да":
    serverPVP = "true"
else:
    serverPVP = "false"
#дальше самое интересное!
#идет вызов функции записи данных в файл
#и для записи передается огромная переменная
#которая тут-же и изменяется.
#в той базе сервера заготовлен конфиг
#с уже заготовленными параметрами, а
#эта программа просто заменяет те значения на
#другие, который ввел пользователь
superDuperCustomConfig = servProperties.replace("server-port=RESERV", "server-port=" + serverPort).replace("online-mode=RESERV", "online-mode=" + serverMode).replace("motd=RESERV", "motd=" + serverName).replace("pvp=RESERV", "pvp=" + serverPVP).replace("max-players=RESERV", "max-players=" + serverMaxPlayers).replace("enable-command-block=RESERV", "enable-command-block=" + serverCBE).replace("gamemode=RESERV", "gamemode=" + gameMode).replace("difficulty=RESERV", "difficulty=" + serverDiff)
essentials.textToFile("server/server.properties", superDuperCustomConfig)
#мне лень дальше комментировать все это
#надеюсь что ты не глупый человек и сам
#сможешь в этом разрбраться...
if platform.system() == "Windows":
    essentials.textToFile("server/start.bat", "@echo Reserv-Server\njava -Xmx1024M -Xms1024M -jar " + serverCore + ".jar nogui\n@PAUSE")
else:
    essentials.textToFile("server/start.sh", "echo \"Reserv-Server\"\njava -Xmx1024M -Xms1024M -jar " + serverCore + ".jar nogui")

creatingWindow.changeText("Всё готово!")
creatingWindow.end()