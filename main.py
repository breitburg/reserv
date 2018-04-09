from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont, QIcon, QPixmap, QDesktopServices
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication, QMessageBox, QLabel, QLineEdit, QCheckBox, QComboBox, QListView, QFileDialog, QProgressBar, QInputDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject
from PyQt5 import QtCore
from PyQt5.QtCore import QThread, QUrl
import sys, platform, requests, wget, time, zipfile, os, lang

INSTALLEDlANG = lang.EN
WINDOWS = "Windows"
DARWIN = "Darwin"
__version__ = "1.1"

class UVar():
    def __init__(self):
        self.var = None

    def setr(self,value):
        self.var = value

    def getr(self):
        return self.var

class buildingLabelChanger(QObject):
    changeSignal = pyqtSignal()

    def setText(self,text):
        self.var.setr(text)
        self.changeSignal.emit()

    def setChangeVar(self,var):
        self.var = var

buildingLabelChanger = buildingLabelChanger()

class endShower(QObject):
    signal = pyqtSignal()

endShower = endShower()

class setrProgressProgressbar(QObject):
    signal = pyqtSignal(int)

setrProgressProgressbar = setrProgressProgressbar()

class setrMaxProgressProgressbar(QObject):
    signal = pyqtSignal(int)

setrMaxProgressProgressbar = setrMaxProgressProgressbar()

class Thread():
    def __new__(cls,func):
        class wrapper(QThread):
            def __init__(self):
                super().__init__()

            def run(self):
                func()

        return wrapper()

class Layer():
    elements = []

    def __init__(self, window):
        raise NotImplementedError()

    def hideElements(self):
        for element in self.elements:
            element.hide()

    def showElements(self):
        for element in self.elements:
            element.show()

class main(QtWidgets.QMainWindow):
    class welcomeLayer(Layer):
        def go_next(self):
            objWelcomeLayer.hideElements()
            objSetingsLayer.showElements()
        def go_back(self):
            objWelcomeLayer.showElements()
            objSetingsLayer.hideElements()
        def open_update(self, event):
            QDesktopServices.openUrl(QUrl(requests.get("http://upbits.org/reserv/lv.txt").text.split()[1]))
        def __init__(self, window):
            if requests.get("http://upbits.org/reserv/lv.txt").text.split()[0] != str(__version__):
                newver_pic = QLabel(window)
                if INSTALLEDlANG == lang.RU:
                    pixmap = QPixmap('new_version_banner_ru.png')
                elif INSTALLEDlANG == lang.EN:
                    pixmap = QPixmap('new_version_banner_en.png')
                newver_pic.setPixmap(pixmap)
                newver_pic.mousePressEvent = self.open_update
                newver_pic.setOpenExternalLinks(True)
                newver_pic.resize(pixmap.width(), pixmap.height())

            next_button = QtWidgets.QPushButton(window)
            next_button.setText(INSTALLEDlANG["nextButton"])
            next_button.clicked.connect(self.go_next)

            copyright_label = QLabel("Copyright © Upbits, 2018\nhttp://upbits.org/", window)

            title_pic = QLabel(window)
            pixmap = QPixmap('logo.png')
            title_pic.setPixmap(pixmap)
            title_pic.resize(pixmap.width(), pixmap.height())
            title_pic.move(190, 150)

            if platform.system() == DARWIN:
                copyright_label.resize(163, 35)
                copyright_label.move(25, 310)

                next_button.resize(147, 32)
                next_button.move(430, 320)
            else:
                copyright_label.resize(160, 30)
                copyright_label.move(25, 325)

                next_button.resize(125, 25)
                next_button.move(450, 330)

            self.elements = [next_button, copyright_label, title_pic]
            if requests.get("http://upbits.org/reserv/lv.txt").text.split()[0] != str(__version__):
                self.elements.append(newver_pic)

    class settingsLayer(Layer):
        def go_next(self):
            objSetingsLayer.hideElements()
            objPluginsLayer.showElements()
        def go_back(self):
            objSetingsLayer.showElements()
            objPluginsLayer.hideElements()
        def __init__(self, window):
            next_button = QtWidgets.QPushButton(window)
            next_button.setText(INSTALLEDlANG["nextButton"])
            next_button.clicked.connect(self.go_next)

            back_button = QtWidgets.QPushButton(window)
            back_button.setText(INSTALLEDlANG["backButton"])
            back_button.clicked.connect(objWelcomeLayer.go_back)

            serverMotdLabel = QLabel(INSTALLEDlANG["descServer"], window)
            self.serverMotdEntry = QLineEdit(window)
            self.serverMotdEntry.setText("Reserv Server")

            serverPortLabel = QLabel(INSTALLEDlANG["serverPort"], window)
            self.serverPortEntry = QLineEdit(window)
            self.serverPortEntry.setText("25565")

            serverMaxPlayersLabel = QLabel(INSTALLEDlANG["playersCount"], window)
            self.serverMaxPlayersEntry = QLineEdit(window)
            self.serverMaxPlayersEntry.setText("20")

            self.serverOnlineModeCheckbox = QCheckBox(INSTALLEDlANG["onlineMode"], window)
            self.serverOnlineModeCheckbox.setChecked(True)

            self.serverCommandBlockEnableCheckbox = QCheckBox(INSTALLEDlANG["commandBlocks"], window)
            self.serverPVPCheckbox = QCheckBox(INSTALLEDlANG["allowPVP"], window)
            self.serverPVPCheckbox.setChecked(True)

            serverDifficultyLabel = QLabel(INSTALLEDlANG["serverDifficulty"], window)
            self.serverDifficultyCombobox = QComboBox(window)
            self.serverDifficultyCombobox.addItems(INSTALLEDlANG["difficultyList"])

            serverVersionLabel = QLabel(INSTALLEDlANG["serverVersion"], window)
            self.serverVersionCombobox = QComboBox(window)
            self.serverVersionCombobox.addItems(requests.get("http://upbits.org/reserv/cores/cores_list.txt").text.split())
            if platform.system() == DARWIN:
                serverMotdLabel.resize(125, 15)
                serverMotdLabel.move(70, 50)
                self.serverMotdEntry.move(70, 70)
                self.serverMotdEntry.resize(200, 23)

                serverPortLabel.resize(125, 15)
                serverPortLabel.move(70, 110)
                self.serverPortEntry.move(70, 130)
                self.serverPortEntry.resize(200, 23)

                serverMaxPlayersLabel.resize(125, 15)
                serverMaxPlayersLabel.move(70, 170)
                self.serverMaxPlayersEntry.move(70, 190)
                self.serverMaxPlayersEntry.resize(200, 23)

                self.serverOnlineModeCheckbox.move(70, 230)
                self.serverOnlineModeCheckbox.resize(130, 15)

                self.serverCommandBlockEnableCheckbox.move(70, 260)
                self.serverCommandBlockEnableCheckbox.resize(140, 15)

                self.serverPVPCheckbox.move(70, 290)
                self.serverPVPCheckbox.resize(130, 15)

                serverDifficultyLabel.move(330, 55)
                serverDifficultyLabel.resize(125, 15)
                self.serverDifficultyCombobox.move(330, 70)
                self.serverDifficultyCombobox.resize(200, 35)

                serverVersionLabel.move(330, 110)
                serverVersionLabel.resize(125, 15)
                self.serverVersionCombobox.move(330, 125)
                self.serverVersionCombobox.resize(200, 35)

                next_button.resize(147, 32)
                next_button.move(430, 320)

                back_button.resize(147, 32)
                back_button.move(280, 320)
            else:
                serverMotdLabel.resize(125, 15)
                serverMotdLabel.move(70, 50)
                self.serverMotdEntry.move(70, 70)
                self.serverMotdEntry.resize(200, 23)

                serverPortLabel.resize(125, 15)
                serverPortLabel.move(70, 110)
                self.serverPortEntry.move(70, 130)
                self.serverPortEntry.resize(200, 23)

                serverMaxPlayersLabel.resize(125, 15)
                serverMaxPlayersLabel.move(70, 170)
                self.serverMaxPlayersEntry.move(70, 190)
                self.serverMaxPlayersEntry.resize(200, 23)

                self.serverOnlineModeCheckbox.move(70, 230)
                self.serverOnlineModeCheckbox.resize(130, 15)

                self.serverCommandBlockEnableCheckbox.move(70, 260)
                self.serverCommandBlockEnableCheckbox.resize(140, 15)

                self.serverPVPCheckbox.move(70, 290)
                self.serverPVPCheckbox.resize(130, 15)

                serverDifficultyLabel.move(330, 50)
                serverDifficultyLabel.resize(125, 15)
                self.serverDifficultyCombobox.move(330, 70)
                self.serverDifficultyCombobox.resize(150, 22)

                serverVersionLabel.move(330, 110)
                serverVersionLabel.resize(125, 15)
                self.serverVersionCombobox.move(330, 125)
                self.serverVersionCombobox.resize(150, 22)

                next_button.resize(125, 25)
                next_button.move(450, 330)

                back_button.resize(125, 25)
                back_button.move(315, 330)

            self.elements = [serverMotdLabel, self.serverMotdEntry, serverPortLabel,
            self.serverPortEntry, serverMaxPlayersLabel, self.serverMaxPlayersEntry, self.serverOnlineModeCheckbox,
            self.serverCommandBlockEnableCheckbox, self.serverPVPCheckbox, next_button, serverDifficultyLabel,
            self.serverDifficultyCombobox, serverVersionLabel, self.serverVersionCombobox, back_button]
            self.hideElements()

    class pluginsLayer(Layer):
        def go_next(self):
            objPluginsLayer.hideElements()
            objSaveServLayer.showElements()
        def go_back(self):
            objPluginsLayer.showElements()
            objSaveServLayer.hideElements()
        def __init__(self, window):
            next_button = QtWidgets.QPushButton(window)
            next_button.setText(INSTALLEDlANG["nextButton"])
            next_button.clicked.connect(self.go_next)

            back_button = QtWidgets.QPushButton(window)
            back_button.setText(INSTALLEDlANG["backButton"])

            infoPlugLabel = QLabel(INSTALLEDlANG["choosePluginsToInstall"], window)

            pluginsList = QListView(window)
            back_button.clicked.connect(objSetingsLayer.go_back)

            if platform.system() == DARWIN:
                infoPlugLabel.move(70, 50)
                infoPlugLabel.resize(350, 15)

                pluginsList.resize(450, 200)
                pluginsList.move(70, 70)

                next_button.resize(147, 32)
                next_button.move(430, 320)

                back_button.resize(147, 32)
                back_button.move(280, 320)
            else:
                infoPlugLabel.move(40,30)
                infoPlugLabel.resize(350, 15)

                pluginsList.resize(510, 250)
                pluginsList.move(40,60)

                next_button.resize(125, 25)
                next_button.move(450, 330)

                back_button.resize(125, 25)
                back_button.move(315, 330)

            model = QStandardItemModel()

            global plugsDict
            plugsDict = {}
            for plugName in requests.get("http://upbits.org/reserv/plugins/plugins_list.txt").text.split():
                plugItem = QStandardItem(plugName)
                plugItem.setCheckable(True)
                plugItem.setEditable(False)
                model.appendRow(plugItem)
                plugsDict[plugName] = plugItem

            pluginsList.setModel(model)

            self.elements = [next_button,infoPlugLabel,pluginsList, back_button]
            self.hideElements()

    class saveServLayer(Layer):
        def go_next(self):
            objSaveServLayer.hideElements()
            objBuildingLayer.showElements()
            self.window.serverBuildThread.start()

        def openDir(self):
            self.serverSavePath = QFileDialog.getExistingDirectory(self.window, INSTALLEDlANG["chooseDirectory"])
            self.directoryEntry.setText(self.serverSavePath)
            if self.serverSavePath != "":
                self.next_button.setDisabled(False)
            else:
                self.next_button.setDisabled(True)

        def __init__(self, window):
            self.window = window
            self.next_button = QtWidgets.QPushButton(window)
            self.next_button.setText(INSTALLEDlANG["buildButton"])
            self.next_button.clicked.connect(self.go_next)
            self.next_button.setDisabled(True)

            back_button = QtWidgets.QPushButton(window)
            back_button.setText(INSTALLEDlANG["backButton"])
            back_button.clicked.connect(objPluginsLayer.go_back)

            serverDirLabel = QLabel(INSTALLEDlANG["chooseDirectoryToSaveServer"], window)
            serverDirLabel.resize(500, 15)

            openDir_button = QtWidgets.QPushButton(window)
            openDir_button.setText(INSTALLEDlANG["chooseDirectory"])
            openDir_button.clicked.connect(self.openDir)

            self.directoryEntry = QLineEdit(window)
            self.directoryEntry.setDisabled(True)
            self.directoryEntry.resize(200, 23)

            if platform.system() == DARWIN:
                self.next_button.resize(147, 32)
                self.next_button.move(430, 320)

                back_button.resize(147, 32)
                back_button.move(280, 320)

                serverDirLabel.move(55, 150)
                openDir_button.resize(147, 32)
                openDir_button.move(220, 175)

                self.directoryEntry.move(192, 210)
            else:
                self.next_button.resize(125, 25)
                self.next_button.move(450, 330)

                back_button.resize(125, 25)
                back_button.move(315, 330)

                serverDirLabel.move(110, 150)

                openDir_button.resize(140, 25)
                openDir_button.move(235, 180)

                self.directoryEntry.move(203, 210)

            self.elements = [self.next_button, back_button, openDir_button, serverDirLabel, self.directoryEntry]
            self.hideElements()

    class buildingLayer(Layer):
        textVar = UVar()

        def progressbar_gui(self, current, total, width=None):
            setrProgressProgressbar.signal.emit(int((current / total) * 100))

        def changeText(self):
            self.buildingLabel.setText(self.textVar.getr())

        def __init__(self, window):
            self.buildingLabel = QLabel(INSTALLEDlANG["pleaseWaitServerBuilding"], window)
            buildingLabelChanger.changeSignal.connect(self.changeText)
            buildingLabelChanger.setChangeVar(self.textVar)
            self.progressBar = QProgressBar(window)
            self.progressBar.setMinimum(0)
            self.progressBar.setMaximum(0)
            self.progressBar.setValue(0)
            setrProgressProgressbar.signal.connect(self.progressBar.setValue)
            setrMaxProgressProgressbar.signal.connect(self.progressBar.setMaximum)

            if platform.system() == DARWIN:
                self.buildingLabel.move(100, 160)
                self.buildingLabel.resize(600, 15)

                self.progressBar.resize(400, 15)
                self.progressBar.move(100, 180)
            else:
                self.buildingLabel.move(100, 160)
                self.buildingLabel.resize(600, 15)

                self.progressBar.resize(400, 15)
                self.progressBar.move(100, 180)

            self.elements = [self.buildingLabel, self.progressBar]
            self.hideElements()

    class wellDoneLayer(Layer):
        def show_done(self):
            objBuildingLayer.hideElements()
            objDoneLayer.showElements()
        def open_donate(self):
            QDesktopServices.openUrl(QUrl("http://www.donationalerts.ru/c/upbits"))
        def exit(self):
            app.exit()
        def __init__(self, window):
            done_label = QLabel(INSTALLEDlANG["wellDone"], window)
            back_pic = QLabel(window)
            pixmap = QPixmap('done_pic.png')
            back_pic.setPixmap(pixmap)
            back_pic.resize(pixmap.width(), pixmap.height())

            donate_button = QtWidgets.QPushButton(window)
            donate_button.setText(INSTALLEDlANG["donateButton"])
            donate_button.clicked.connect(self.open_donate)

            close_button = QtWidgets.QPushButton(window)
            close_button.setText(INSTALLEDlANG["closeButton"])
            close_button.clicked.connect(self.exit)

            if platform.system() == DARWIN:
                done_label.resize(500, 28)
                done_label.move(250, 140)

                donate_button.resize(147, 32)
                donate_button.move(420, 173)

                close_button.resize(147, 32)
                close_button.move(278, 173)
            else:
                done_label.resize(500, 40)
                done_label.move(250, 120)

                donate_button.resize(130, 25)
                donate_button.move(420, 173)

                close_button.resize(130, 25)
                close_button.move(278, 173)

            self.elements = [back_pic, done_label, donate_button, close_button]
            self.hideElements()

    @Thread
    def serverBuildThread():
        #print(objSetingsLayer.serverPVPCheckbox.isChecked())
        #objSetingsLayer.serverMotdEntry.text()
        #objSetingsLayer.serverVersionCombobox.currentText()
        buildingLabelChanger.setText(INSTALLEDlANG["downloadingServer"])
        setrMaxProgressProgressbar.signal.emit(100)
        wget.download("http://upbits.org/reserv/bundle.zip", objSaveServLayer.serverSavePath + "/server.zip", bar=objBuildingLayer.progressbar_gui)
        setrProgressProgressbar.signal.emit(0)
        setrMaxProgressProgressbar.signal.emit(0)
        buildingLabelChanger.setText(INSTALLEDlANG["unpackingServer"])

        with zipfile.ZipFile(objSaveServLayer.serverSavePath + "/server.zip", "r") as zip_ref:
            zip_ref.extractall(objSaveServLayer.serverSavePath + "/" + objSetingsLayer.serverMotdEntry.text())

        buildingLabelChanger.setText(INSTALLEDlANG["removeCache"])
        os.remove(objSaveServLayer.serverSavePath + "/server.zip")
        buildingLabelChanger.setText(INSTALLEDlANG["downloadingCore"])
        setrMaxProgressProgressbar.signal.emit(100)
        wget.download("http://upbits.org/reserv/cores/" + objSetingsLayer.serverVersionCombobox.currentText() + ".jar", objSaveServLayer.serverSavePath + "/" + objSetingsLayer.serverMotdEntry.text(), bar=objBuildingLayer.progressbar_gui)
        setrProgressProgressbar.signal.emit(0)
        setrMaxProgressProgressbar.signal.emit(0)
        for plug in plugsDict.items():
            if plug[1].checkState() == 2:
                buildingLabelChanger.setText(INSTALLEDlANG["downloading"] + plug[0] + "...")
                setrMaxProgressProgressbar.signal.emit(100)
                wget.download("http://upbits.org/reserv/plugins/" + plug[0] + ".jar", objSaveServLayer.serverSavePath + "/" + objSetingsLayer.serverMotdEntry.text() + "/plugins/", bar=objBuildingLayer.progressbar_gui)
                setrProgressProgressbar.signal.emit(0)
        setrMaxProgressProgressbar.signal.emit(0)

        buildingLabelChanger.setText(INSTALLEDlANG["settings"])
        file_contains = open(objSaveServLayer.serverSavePath + "/" + objSetingsLayer.serverMotdEntry.text() + "/server.properties", "r").read()
        if objSetingsLayer.serverDifficultyCombobox.currentText() == INSTALLEDlANG["difficultyList"][0]:
            serverDiff = "0"
        elif objSetingsLayer.serverDifficultyCombobox.currentText() == INSTALLEDlANG["difficultyList"][1]:
            serverDiff = "1"
        elif objSetingsLayer.serverDifficultyCombobox.currentText() == INSTALLEDlANG["difficultyList"][2]:
            serverDiff = "2"
        else:
            serverDiff = "3"

        with open(objSaveServLayer.serverSavePath + "/" + objSetingsLayer.serverMotdEntry.text() + "/server.properties","w+") as file_save:
            config = file_contains.replace("server-port=RESERV", "server-port=" + objSetingsLayer.serverPortEntry.text()).replace("online-mode=RESERV", "online-mode=" + str(objSetingsLayer.serverOnlineModeCheckbox.isChecked()).lower()).replace("motd=RESERV", "motd=" + objSetingsLayer.serverMotdEntry.text()).replace("pvp=RESERV", "pvp=" + str(objSetingsLayer.serverPVPCheckbox.isChecked()).lower()).replace("max-players=RESERV", "max-players=" + objSetingsLayer.serverMaxPlayersEntry.text()).replace("enable-command-block=RESERV", "enable-command-block=" + str(objSetingsLayer.serverCommandBlockEnableCheckbox.isChecked()).lower()).replace("difficulty=RESERV", "difficulty=" + serverDiff)
            file_save.write(config)

        if platform.system() == DARWIN:
            with open(objSaveServLayer.serverSavePath + "/" + objSetingsLayer.serverMotdEntry.text() + "/start.command","w+") as autostart_save:
                autostart_save.write("echo \"Reserv-Server\"\njava -Xmx1024M -Xms1024M -jar " + objSetingsLayer.serverVersionCombobox.currentText() + ".jar nogui_old")
        elif platform.system() == WINDOWS:
            with open(objSaveServLayer.serverSavePath + "/" + objSetingsLayer.serverMotdEntry.text() + "/start.bat","w+") as autostart_save:
                autostart_save.write("@echo Reserv-Server\njava -Xmx1024M -Xms1024M -jar " + objSetingsLayer.serverVersionCombobox.currentText() + ".jar nogui_old\n@PAUSE")
        else:
            with open(objSaveServLayer.serverSavePath + "/" + objSetingsLayer.serverMotdEntry.text() + "/start.sh","w+") as autostart_save:
                autostart_save.write("echo \"Reserv-Server\"\njava -Xmx1024M -Xms1024M -jar " + objSetingsLayer.serverVersionCombobox.currentText() + ".jar nogui_old")

        endShower.signal.emit()

    def __init__(self):
        global INSTALLEDlANG
        super().__init__()
        item, ok = QInputDialog.getItem(self, "Language", "Select your language:", lang.langsList, 0, False)
        if ok and item:
            if item == lang.langsList[0]:
                INSTALLEDlANG = lang.RU
            elif item == lang.langsList[1]:
                INSTALLEDlANG = lang.EN
        else:
            QMessageBox.critical(self, "Select language", "Please select the language next time.")
            quit()
        try:
            requests.get("http://upbits.org/")
        except:
            QMessageBox.critical(self, INSTALLEDlANG["connectError"], INSTALLEDlANG["connectErrorText"])
            app.exit()
        if platform.system() == WINDOWS:
            self.setWindowIcon(QIcon('win_icon.ico'))
        if platform.system() == DARWIN:
            self.setFixedSize(598, 362)
        else:
            self.setFixedSize(600, 370)
        self.setWindowTitle("Reserv")

        global objWelcomeLayer
        global objSetingsLayer
        global objPluginsLayer
        global objSaveServLayer
        global objBuildingLayer
        global objDoneLayer
        objWelcomeLayer = self.welcomeLayer(self)
        objSetingsLayer = self.settingsLayer(self)
        objPluginsLayer = self.pluginsLayer(self)
        objSaveServLayer = self.saveServLayer(self)
        objBuildingLayer = self.buildingLayer(self)
        objDoneLayer = self.wellDoneLayer(self)
        endShower.signal.connect(objDoneLayer.show_done)
        self.showNormal()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    objMain = main()
    sys.exit(app.exec_())
