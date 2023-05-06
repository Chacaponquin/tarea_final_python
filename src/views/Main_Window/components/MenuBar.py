from src.views.Main_Window.Main_Window_Controller import MainWindowController
from PyQt6 import QtWidgets


class MenuBar:
    def __init__(self, main_window_controller: MainWindowController):
        self.main_window_controller = main_window_controller

    def create_menu_bar(self):
        # create menu
        menubar = QtWidgets.QWidget()

        menu_bar_layout = QtWidgets.QHBoxLayout()
        menubar.setLayout(menu_bar_layout)

        import_button = QtWidgets.QPushButton('Import')
        import_button.setStyleSheet('background-color: green; color: white; font-size: 20px; font-weight: 600')
        import_button.setFixedWidth(150)

        menu_bar_layout.addWidget(import_button)

        return menubar
