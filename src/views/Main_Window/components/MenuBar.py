from src.views.Main_Window.Main_Window_Controller import MainWindowController
from PyQt6 import QtWidgets, QtGui, QtCore


class MenuBar:
    def __init__(self, main_window_controller: MainWindowController):
        self.main_window_controller = main_window_controller

        # create menu
        self.menubar = QtWidgets.QWidget()

        self.menu_bar_layout = QtWidgets.QHBoxLayout(self.menubar)
        self.menubar.setLayout(self.menu_bar_layout)

        import_button = QtWidgets.QPushButton('Import')
        import_button.clicked.connect(lambda x: self.load_txt())
        import_button.setStyleSheet('background-color: green; color: white; font-size: 20px; font-weight: 600')
        import_button.setFixedWidth(150)

        self.menu_bar_layout.addWidget(import_button)

    def create_menu_bar(self):
        return self.menubar

    def load_txt(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("Text files (*.txt)")
        dialog.setViewMode(QtWidgets.QFileDialog.ViewMode.List)

        if dialog.exec():
            filenames = dialog.selectedFiles()
            print(filenames)

            self.main_window_controller.import_txts(filenames)
