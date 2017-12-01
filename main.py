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

serverName = ""
serverMode = ""
serverPort = ""
serverRcon = ""
global serverName
global serverMode
global serverRcon
global serverPort

def basicConfigurate():
    essintials.universalClear()
    serverName = input("- Мастер конфигурации Reserv -\nДля дальнейшей сборки сервера просим вас пройти первоначальную настройку всех параметров по которым в дальшейшем будет собран ваш сервер.\n\nВведите название сервера: ")
    serverPort = input("Какой порт вы желаете использовать? (по-умолчанию 25565) ")
    if serverPort == "":
        print("Устанавливаем порт 25565. Как по-умолчанию.")
        serverPort = "25565"

    serverMode = input("Допускать не лицензированные копии игры на сервер? (да/нет) ")
    if serverMode != "да" and serverMode != "нет":
        print("Эм.. " + serverMode + "? Что? Не понял.. Короче, сделаем так чтоб всех пускало, а то ты какой-то непонятный.")
        serverMode = "нет"

    serverRcon = input("Хотите-ли использовать протокол удаленного управления сервером RCON? (да/нет) ")
    if serverRcon == "да":
        rconPort = input("Ох, ну раз так введите желаемый порт для RCON: ")
        rconPassword = input("Осталось только ввести пароль (только англ.): ")
        print("Протокол RCON успешно конфигурирован.")
    elif serverRcon != "нет":
        print("Эм.. " + serverRcon + "? Что? Короче нахрен вырубим лучше этот RCON, а то еще взломает кто.")
        serverRcon = "нет"
    if input("\nКонфигурация сервера успешно проведена. Давайте проверим, всем ли вы удовлетворены.\nИмя: " + serverName + "\nПорт: " + serverPort + "\nОнлайн-режим: " + serverMode + "\nRcon: " + serverRcon + "\nВсе нормально? (да/нет) ") == "да":
        if serverMode == "да":
            serverMode = "true"
        else:
            serverMode = "false"
        if serverRcon == "да":
            serverRcon = "true"
        else:
            serverRcon = "false"

        advncConfigurate()
    else:
        basicConfigurate()

def advncConfigurate():
    essintials.universalClear()
    serverCore = input("- Конфигурация ядра Reserv - \n\nВыберите версию ядра из предложенных (1.12, 1.11, 1.10, 1.9, 1.8): ")
    if serverCore == "1.12" or serverCore == "1.11" or serverCore == "1.10" or serverCore == "1.9" or serverCore == "1.8":
        print("Установлена версия ядра " + serverCore + ".")
    else:
        print("Какая-то странная версия у тебя. " + serverCore + ". Кажись такой у нас нет. Поставим тебе последнюю.")
        serverCore = "1.12"
    essintials.universalClear()
    if input("Конфигурация была завершена. Начать сборку сервера? (да/нет)") == "да":
        essintials.universalClear()
        print("Загрузка сервера...")
        wget.download("http://hack.blinkhub.ru/reserv/server.zip")
        print("Распаковка сервера...")
        essintials.unZip("server.zip", "server/")
        os.remove("server.zip")
        print("Загрузка ядра....")
        wget.download("http://hack.blinkhub.ru/reserv/cores/" + serverCore + ".jar", "server/")
        print("Настройка параметров...")
        servProperties = essintials.textFromFile("server/server.properties")
        global serverName
        global serverMode
        global serverRcon
        global serverPort
        essintials.textToFile(servProperties.replace("server-port=RESERV", "server-port=" + serverPort).replace("online-mode=RESERV", "online-mode=" + serverMode).replace("motd=RESERV", "motd=" + serverName).replace("enable-rcon=RESERV", "enable-rcon=" + serverRcon), "server/server.properties")
        print("Сборка сервера завершена.")



#тут начало исполняемого кода

essintials.universalClear()
userChoice = input("Reserv " + essintials.colorText("(первая сборка)", "red") + "\nCopyright © Ketsu8, All rights reserved\nGithub: http://github.com/Upbits/Reserv\n\n(Z) Нормальный запуск. Так-как будет у обычных людей.\n(A) Базовая конфигурация\n(B) Продвинутая конфигурация\n(C) Сборка сервера\n")
if userChoice == "Z" or userChoice == "z":
    if input("- Лицензионное соглашение Mojang -\nЛицензионное соглашение: https://account.mojang.com/terms\n\nПомните, что все права на исходные коды серверов и плагинов пренадлежат из владельцам. Мы никоем оброзам не пытаемся присвоить из себе.\n\nЯ согласен(а)? (да/нет) ") == "да":
        basicConfigurate()
    else:
        print("Ну ладно. Тогда пока.")
        quit(0)
elif userChoice == "A" or userChoice == "a":
    basicConfigurate()
elif userChoice == "B" or userChoice == "b":
    advncConfigurate()
elif userChoice == "C" or userChoice == "c":
    print("Сборки пока нет. хдхдхдхдхдхдхдхд завтра ее сделаю")
