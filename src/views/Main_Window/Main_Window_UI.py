from PyQt6 import QtWidgets
from .Main_Window_Controller import MainWindowController
from .components import FormSection, MenuBar, ImageSection
from .constants import VIEWS


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.views: dict = {}

        self.main_window_controller = MainWindowController(self.views)

        self.init_ui()

    def init_ui(self):
        # Configurar la ventana
        self.setWindowTitle("Graph App")
        self.setGeometry(0, 0, 1200, 750)

        widget = QtWidgets.QWidget()

        # Crear un grid-layout con dos secciones
        layout = QtWidgets.QGridLayout(widget)

        content = QtWidgets.QWidget()
        content_layout = QtWidgets.QGridLayout(content)

        self.views[VIEWS.MENU_BAR] = MenuBar(layout, self.main_window_controller)
        self.views[VIEWS.FORM_SECTION] = FormSection(content_layout, self.main_window_controller)
        self.views[VIEWS.IMAGE_SECTION] = ImageSection(content_layout, self.main_window_controller)

        # Añadir la sección de la imagen a la parte inferior del grid-layout
        layout.addWidget(content, 1, 0)

        self.setCentralWidget(widget)



