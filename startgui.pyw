'''
Reserv GUI

Copyright © Upbits Team, 2017 – 2018.
GitHub: http://github.com/Upbits/

По вопросом Reserv писать сюда:
https://vk.com/upbits или на почту
<upbits@blinkhub.ru>.

Удачного использования :D
'''

import platform
from tkinter import messagebox

if platform.system() == "Darwin":
    messagebox.showerror(title="Ошибка", message="Извините, но macOS не поддерживается. Для обратной связи обратитесь в поддержку.")
    quit()

try:
    import os, zipfile, wget, essentials, time, requests, gui, belfrywidgets, threading, sys #импорт всех нужных библиотек
except:
    import platform, os, time
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    if messagebox.askokcancel(title="Ошибка", message="У вас не найдены некоторые библиотеки которые требуются для работы программы. Установить их?") == True:
        if platform.system() == "Windows":
            os.system("pip3 install wget requests belfrywidgets colorama")
        elif platform.system() == "Linux":
            os.system("sudo pip3 install wget requests belfrywidgets colorama && sudo apt install python3-tk")
        else:
            os.system("sudo pip3 install wget requests belfrywidgets colorama")
        messagebox.showinfo(title="Готово", message="Все библиотеки успешно установлены. Пожалуйста перезапустите Reserv.")
        quit()
    else:
        quit()
welcome = gui.showWelcomeWindow()
welcome.show()


config = gui.showSettingsWindow()
s = config.show(None, None, None, None, None, None, None)
serverName = s[1]
serverPort = s[2]

if serverName == "":
    serverName = "Reserv Server"

if serverPort == "":
    serverPort = "25565"

serverMode = s[3]

serverMaxPlayers = s[6]
if serverMaxPlayers == "":
    serverMaxPlayers = "20"

serverCBE = s[4]

serverPVP = s[5]

serverDiff = s[7]

gameMode = s[8]

ver = gui.showVersionWindow()
verList = requests.get("http://ketsu8.ru/reserv/cores/cores_list.txt").text.split()
choosedVersion = ver.show(verList, None)
serverCore = str(verList[int(choosedVersion[1]) - 1])

plug = gui.showPluginWindow()
pluginsList = requests.get("http://ketsu8.ru/reserv/plugins/plugins_list.txt").text.split()
selectedPlugins = plug.show(PluginsArray=pluginsList)
pluginToInstall = []
for plugin_it in selectedPlugins:
    if selectedPlugins[plugin_it].get() == True:
        pluginToInstall.append(plugin_it)

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
wget.download("http://ketsu8.ru/reserv/bundle.zip", "server.zip")
creatingWindow.changeText("Распаковка сервера...")
essentials.unZip("server.zip", "server/")
os.remove("server.zip")
creatingWindow.changeText("Загрузка ядра....")
wget.download("http://ketsu8.ru/reserv/cores/" + serverCore + ".jar", "server/")
creatingWindow.changeText("\nУстановка плагинов...")

for plugin in pluginToInstall:
    creatingWindow.changeText("\nЗагрузка " + plugin + "...")
    wget.download("http://ketsu8.ru/reserv/plugins/" + plugin + ".jar", "server/plugins/")
    creatingWindow.changeText("\nПлагин " + plugin + " установлен...")

creatingWindow.changeText("\nНастройка параметров...")
servProperties = essentials.textFromFile("server/server.properties")
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
superDuperCustomConfig = servProperties.replace("server-port=RESERV", "server-port=" + serverPort).replace("online-mode=RESERV", "online-mode=" + serverMode).replace("motd=RESERV", "motd=" + serverName).replace("pvp=RESERV", "pvp=" + serverPVP).replace("max-players=RESERV", "max-players=" + serverMaxPlayers).replace("enable-command-block=RESERV", "enable-command-block=" + serverCBE).replace("gamemode=RESERV", "gamemode=" + gameMode).replace("difficulty=RESERV", "difficulty=" + serverDiff)
essentials.textToFile("server/server.properties", superDuperCustomConfig)
if platform.system() == "Windows":
    essentials.textToFile("server/start.bat", "@echo Reserv-Server\njava -Xmx1024M -Xms1024M -jar " + serverCore + ".jar nogui\n@PAUSE")
else:
    essentials.textToFile("server/start.sh", "echo \"Reserv-Server\"\njava -Xmx1024M -Xms1024M -jar " + serverCore + ".jar nogui")
creatingWindow.changeText("Всё готово!")
creatingWindow.end()
