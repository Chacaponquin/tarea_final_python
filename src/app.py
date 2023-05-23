import sys
from PyQt6 import QtWidgets
from src.views.Main_Window.Main_Window_UI import MainWindow
from qt_material import apply_stylesheet

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    apply_stylesheet(app, theme='light_blue.xml')
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
