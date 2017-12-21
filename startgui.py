print("Запуск Reserv с интегрированым интерфейсом.")
import gui

objWelcomeWindow = gui.showWelcomeWindow()
objWelcomeWindow.show()

objPathWindow = gui.showPathWindow()
objPathWindow.show()

VersionArray = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]

objVersionWindow = gui.showVersionWindow()
print(objVersionWindow.show(VersionArray))
