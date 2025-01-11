from PyQt5 import QtWidgets
from GUI.FacadeGui import Facade

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Facade()
    u2 = Facade()

    # singleton test
    if id(ui) == id(u2):
        print("Singleton is working")

    else:
        print("Singleton isn`t working!")

    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
