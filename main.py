'''
Reserv - главный скрипт

Copyright © Upbits Team, 2017 – 2018.
GitHub: http://github.com/Upbits/

По вопросом Reserv писать сюда:
https://vk.com/reserv или на почту
<reserv@blinkhub.ru>.

Удачного использования :D
'''

import os
import zipfile
import wget
import essintials

essintials.universalClear()
input("Добро пожаловать в Reserv\nCopyright © Ketsu8, All rights reserved.\nGithub: http://github.com/Upbits/Reserv\n\nНажмите на (Enter) чтобы приступить к сборке собственного сервера Minecraft...\n")
essintials.universalClear()
input("Лицензионное соглашение Reserv\nCopyright © Ketsu8, All rights reserved.\n\nВсе права на исходный код серверов\nи плагинов пренадлежат их праваобладателям.\nМы никоим образом не пытаемся присвоить их себе. В то\nвремя как права на исходный код Reserv пренадлежат\nкоманде UpBits на момент 2017 - 2018г.\n\nЕсли вы согласны, то нажмите на (Enter).\n")
essintials.universalClear()
serverName = input("Сборка сервера Reserv\nCopyright © Ketsu8, All rights reserved.\n\nВведите название сервера: ")
serverPort = input("Какой порт вы желаете использовать? (по-умолчанию 25565) ")
if serverPort == "":
    print("Применена настройка по-умолчанию.")
    serverPort = "25565"

serverMode = input("Допускать не лицензированные копии игры на сервер? (да/нет) ")
if serverMode != "да" and serverMode != "нет":
    print("Применена настройка по-умолчанию.")
    serverMode = "нет"
#нововведения
serverMaxPlayers = input("Введите макисмальное колличество игроков на сервере: ")
if serverMaxPlayers == "":
    print("Применена настройка по-умолчанию.")
    serverMaxPlayers = "20"

serverCBE = input("Разрешить использование командного блока? (да/нет) ")
if serverCBE != "нет" and serverCBE != "да":
    print("Применена настройка по-умолчанию.")
    serverCBE = "нет"

serverPVP = input("Разрешить PVP на вашем сервере? (да/нет) ")
if serverPVP != "нет" and serverPVP != "да":
    print("Применена настройка по-умолчанию.")
    serverPVP = "нет"


serverRcon = input("Хотите-ли использовать протокол удаленного управления сервером RCON? (да/нет) ")
if serverRcon == "да":
    rconPort = input("Ох, ну раз так введите желаемый порт для RCON: ")
    rconPassword = input("Осталось только ввести пароль (только англ.): ")
elif serverRcon != "нет":
    print("Применена настройка по-умолчанию.")
    serverRcon = "нет"

serverCore = input("Выберите версию ядра (c 1.8 по 1.12): ")
if serverCore == "1.12" or serverCore == "1.11" or serverCore == "1.10" or serverCore == "1.9" or serverCore == "1.8":
    print("Установлена версия ядра " + serverCore + ".")
else:
    print("Применена настройка по-умолчанию.")
    serverCore = "1.12"
essintials.universalClear()
if input("Reserv Builder\nCopyright © Ketsu8, All rights reserved\n\nСервер " + serverName + " был успешно сконфигурирован. Вы выбрали версию " + serverCore + ", онлайн-режим установили на " + serverMode + ", использовали порт " + serverPort + " и установили статус RCON на " + serverRcon + ".\n\n(Y) Запустить сборку\n(B) Отменить сборку\n") == "Y":
    essintials.universalClear()
    print("Загрузка сервера...")
    wget.download("http://hack.blinkhub.ru/reserv/server.zip")
    print("Распаковка сервера...")
    essintials.unZip("server.zip", "server/")
    os.remove("server.zip")
    print("Загрузка ядра....")
    wget.download("http://hack.blinkhub.ru/reserv/cores/" + serverCore + ".jar", "server/")
    print("\nНастройка параметров...")
    servProperties = essintials.textFromFile("server/server.properties")
    if serverMode == "да":
        serverMode = "true"
    else:
        serverMode = "false"

    if serverRcon == "да":
        serverRcon = "true"
    else:
        serverRcon = "false"
        rconPassword = "false"
        rconPort = "false"

    if serverCBE == "да":
        serverCBE = "true"
    else:
        serverCBE = "false"

    if serverPVP == "да":
        serverPVP = "true"
    else:
        serverPVP = "false"
    essintials.textToFile("server/server.properties", servProperties.replace("server-port=RESERV", "server-port=" + serverPort).replace("online-mode=RESERV", "online-mode=" + serverMode).replace("motd=RESERV", "motd=" + serverName).replace("enable-rcon=RESERV", "enable-rcon=" + serverRcon).replace("rcon.port=RESERV", "rcon.port=" + rconPort).replace("rcon.password=RESERV", "rcon.password=" + rconPassword).replace("pvp=RESERV", "pvp=" + serverPVP).replace("max-players=RESERV", "max-players=" + serverMaxPlayers).replace("enable-command-block=RESERV", "enable-command-block=" + serverCBE))
    print("\nСборка сервера завершена.")
else:
    print("Отмена сборки сервера.")
    quit(5)
