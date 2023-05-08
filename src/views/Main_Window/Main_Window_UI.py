from PyQt6 import QtWidgets, QtGui, QtCore
from .Main_Window_Controller import MainWindowController
from .components import FormSection, MenuBar, ImageSection


class Signals(QtCore.QObject):
    updateGraphsSignal = QtCore.pyqtSignal()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.signals = Signals()
        self.main_window_controller = MainWindowController(self.signals)

        self.main_window_controller.signals.updateGraphsSignal.connect(lambda x: self.update_graphs())

        self.init_ui()

    def update_graphs(self):
        print('Buenas')

    def init_ui(self):
        # Configurar la ventana
        self.setWindowTitle("Graph App")
        self.setGeometry(0, 0, 1200, 750)

        widget = QtWidgets.QWidget()

        # Crear un grid-layout con dos secciones
        layout = QtWidgets.QGridLayout(widget)

        content = QtWidgets.QWidget()
        content_layout = QtWidgets.QGridLayout(content)

        MenuBar(layout, self.main_window_controller)
        FormSection(content_layout, self.main_window_controller)
        ImageSection(content_layout, self.main_window_controller)

        # Añadir la sección de la imagen a la parte inferior del grid-layout
        layout.addWidget(content, 1, 0)

        self.setCentralWidget(widget)



