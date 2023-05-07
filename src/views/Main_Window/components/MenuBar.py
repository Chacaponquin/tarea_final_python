from src.views.Main_Window.Main_Window_Controller import MainWindowController
from PyQt6 import QtWidgets


class MenuBar:
    def __init__(self, parent_layout: QtWidgets.QGridLayout, main_window_controller: MainWindowController):
        self.main_window_controller = main_window_controller

        # create menu
        self.menubar = QtWidgets.QWidget()
        self.menu_bar_layout = QtWidgets.QHBoxLayout(self.menubar)
        self.menu_bar_layout.setSpacing(15)

        self.menu_bar_layout.addStretch()

        import_button = QtWidgets.QPushButton('Import')
        import_button.clicked.connect(lambda x: self.load_txt())
        import_button.setStyleSheet(
            'background-color: green; color: white; font-size: 18px; font-weight: 600; padding: 3.5px 0'
        )
        import_button.setFixedWidth(100)

        new_graph_button = QtWidgets.QPushButton('New Graph')
        new_graph_button.clicked.connect(lambda x: self.create_new_graph())
        new_graph_button.setStyleSheet(
            'background-color: blue; color: white; font-size: 18px; font-weight: 600; padding: 3.5px 20px'
        )

        self.menu_bar_layout.addWidget(import_button)
        self.menu_bar_layout.addWidget(new_graph_button)

        parent_layout.addWidget(self.menubar, 0, 0)

    def create_new_graph(self):
        self.main_window_controller.add_new_graph()

    def load_txt(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("Text files (*.txt)")
        dialog.setViewMode(QtWidgets.QFileDialog.ViewMode.List)

        if dialog.exec():
            filenames = dialog.selectedFiles()
            print(filenames)

            self.main_window_controller.import_txts(filenames)
