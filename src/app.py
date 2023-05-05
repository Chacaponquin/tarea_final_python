from PyQt6.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        window = QWidget()

        layout = QGridLayout()
        layout.addWidget(QPushButton("Hay que ser feliz"), 0, 0 )
        window.setLayout(layout)

        self.setCentralWidget(window)


if __name__ == '__main__':
    application = QApplication([])
    mainWindow = MainWindow()
    mainWindow.setWindowTitle('Graph Python Project')
    mainWindow.show()
    application.exec()