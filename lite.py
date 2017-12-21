'''
Reserv Lite

Copyright © Upbits Team, 2017 – 2018.
GitHub: http://github.com/Upbits/

По вопросом Reserv писать сюда:
https://vk.com/reserv или на почту
<reserv@blinkhub.ru>.

Удачного использования :D
'''

import os, zipfile, wget, essentials, platform #импорт всех нужных библиотек

essentials.universalClear() #вызов функции универсальной отчистки
input("Добро пожаловать в Reserv\nCopyright © Ketsu8, All rights reserved.\nGithub: http://github.com/Upbits/Reserv\n\nНажмите на (Enter) чтобы приступить к сборке собственного сервера Minecraft...\n")

#код для отображения окна соглашения с лицензией
essentials.universalClear()
input("Лицензионное соглашение Reserv\nCopyright © Ketsu8, All rights reserved.\n\nВсе права на исходный код серверов\nи плагинов пренадлежат их праваобладателям.\nМы никоим образом не пытаемся присвоить их себе. В то\nвремя как права на исходный код Reserv пренадлежат\nкоманде UpBits на момент 2017 - 2018г.\n\nЕсли вы согласны, то нажмите на (Enter).\n")

essentials.universalClear()
#приветствие и ввод адреса сервера
serverName = input("Сборка сервера Reserv\nCopyright © Ketsu8, All rights reserved.\n\nВведите название сервера: ")
serverPort = input("Какой порт вы желаете использовать? (по-умолчанию 25565) ") #ввод порта сервера

if serverPort == "":
    print("Применена настройка по-умолчанию.")
    serverPort = "25565"

#диалоговое окно в терминале кароч
#выбор online-mode на true или false
serverMode = input("Допускать не лицензированные копии игры на сервер? (да/нет) ")
if serverMode != "да" and serverMode != "нет":
    print("Применена настройка по-умолчанию.")
    serverMode = "нет"

#максимальное колличество игроков
serverMaxPlayers = input("Введите макисмальное колличество игроков на сервере: ")
if serverMaxPlayers == "":
    print("Применена настройка по-умолчанию.")
    serverMaxPlayers = "20"

#доступны ли командные блоки на сервере
serverCBE = input("Разрешить использование командного блока? (да/нет) ")
if serverCBE != "нет" and serverCBE != "да":
    print("Применена настройка по-умолчанию.")
    serverCBE = "нет"

#доступно ли PVP
serverPVP = input("Разрешить PVP на вашем сервере? (да/нет) ")
if serverPVP != "нет" and serverPVP != "да":
    print("Применена настройка по-умолчанию.")
    serverPVP = "нет"

#всякий бред про RCON
serverRcon = input("Хотите-ли использовать протокол удаленного управления сервером RCON? (да/нет) ")
if serverRcon == "да": #если пользователь ответил да, то
    rconPort = input("Ох, ну раз так введите желаемый порт для RCON: ") #запрашивается порт
    rconPassword = input("Осталось только ввести пароль (только англ.): ") #и запрашивается пароль
elif serverRcon == "нет":
    print("Ну нет-так нет.") #лучше и не скажешь
    serverRcon = "нет"
else:
    print("Применена настройка по-умолчанию.")
    serverRcon = "нет"

#ядро сервера
serverCore = input("Выберите версию ядра (c 1.8 по 1.12): ")
#потом реализую по-нормальному
#но сейчас и так сойдет!
if serverCore == "1.12" or serverCore == "1.11" or serverCore == "1.10" or serverCore == "1.9" or serverCore == "1.8":
    print("Установлена версия ядра " + serverCore + ".")
else:
    print("Применена настройка по-умолчанию.")
    serverCore = "1.12"
essentials.universalClear()

#начинается полный пипец
isBuild = input("Reserv Builder\nCopyright © Ketsu8, All rights reserved\n\nСервер " + serverName + " был успешно сконфигурирован. Вы выбрали версию " + serverCore + ", онлайн-режим установили на " + serverMode + ", использовали порт " + serverPort + " и установили статус RCON на " + serverRcon + ".\n\n(Y) Запустить сборку\n(B) Отменить сборку\n")
if isBuild == "Y" or isBuild == "":
    essentials.universalClear()
    print("Загрузка сервера...")
    #скачивается база сервера с сервера
    #прямо рекурсия получается
    wget.download("http://hack.blinkhub.ru/reserv/server.zip")
    print("Распаковка сервера...")
    #распаковывается сервер
    #используя функцию unZip из
    #нашей библиотеки Essentials
    essentials.unZip("server.zip", "server/")
    os.remove("server.zip")
    print("Загрузка ядра....")
    #дальше идет загрузка самого важного компанента
    #сервера – ядра... короче просто подставляется 
    #переменная с версией ядра... все очень просто
    #и с костылями конечго-же... потом как-нибуть...
    wget.download("http://hack.blinkhub.ru/reserv/cores/" + serverCore + ".jar", "server/")
    print("\nНастройка параметров...")
    #уу! настройка параметров!
    #готовится самая главная переменная
    #в которую записан весь текст из файла
    #конфигурации сервера Minecraft
    servProperties = essentials.textFromFile("server/server.properties") #вот она это строчка судьбы
    #дальше идет намализация переменных
    #которче, готовится к тому что-бы быть
    #записанным в файл конфига
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
    #дальше самое интересное!
    #идет вызов функции записи данных в файл
    #и для записи передается огромная переменная
    #которая тут-же и изменяется.
    #в той базе сервера заготовлен конфиг
    #с уже заготовленными параметрами, а
    #эта программа просто заменяет те значения на
    #другие, который ввел пользователь
    superDuperCustomConfig = servProperties.replace("server-port=RESERV", "server-port=" + serverPort).replace("online-mode=RESERV", "online-mode=" + serverMode).replace("motd=RESERV", "motd=" + serverName).replace("enable-rcon=RESERV", "enable-rcon=" + serverRcon).replace("rcon.port=RESERV", "rcon.port=" + rconPort).replace("rcon.password=RESERV", "rcon.password=" + rconPassword).replace("pvp=RESERV", "pvp=" + serverPVP).replace("max-players=RESERV", "max-players=" + serverMaxPlayers).replace("enable-command-block=RESERV", "enable-command-block=" + serverCBE)
    essentials.textToFile("server/server.properties", superDuperCustomConfig)

    #мне лень дальше комментировать все это
    #надеюсь что ты не глупый человек и сам
    #сможешь в этом разрбраться...
    maxRAM = input("Введите максимальное колличество ОЗУ в мегабайтах: (по-умолчанию 1024) ")
    if maxRAM == "":
        print("Применена настройка по-умолчанию.")
        maxRAM = "1024"
    elif int(maxRAM) > 2048:
        print(maxRAM + " это слишком много для сервера! Установим 1024MB.")
        maxRAM = "1024"
    else:
        print("Применена настройка по-умолчанию.")
        maxRAM = "1024"
    if platform.system() == "Windows":
        essentials.textToFile("server/start.bat", "@echo Reserv-Server\njava -Xmx" + maxRAM + "M -Xms" + maxRAM + "M -jar " + serverCore + ".jar nogui\n@PAUSE")
    else:
        essentials.textToFile("server/start.sh", "java -Xmx" + maxRAM + "M -Xms" + maxRAM + "M -jar " + serverCore + ".jar nogui")
        os.chmod("server/start.sh", 777)
    if input("Сборка сервера завершена.\nЗапустить сервер сейчас? (да/нет) ") == "да":
        if platform.system() == "Windows":
            os.chdir("server/")
            os.system("start.bat")
        else:
            os.chdir("server/")
            os.system("sh start.sh")
    print("До следующий сборки сервера! Программа создана командой Upbits.\nВКонтакте: https://vk.com/upbits")
else:
    print("Отмена сборки сервера.")
    quit(5)
