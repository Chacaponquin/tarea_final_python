import sys
from PyQt6 import QtWidgets
from src.views.Main_Window.Main_Window_UI import MainWindow

if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.show()
        sys.exit(app.exec())
    except Exception as error:
        print(error)
