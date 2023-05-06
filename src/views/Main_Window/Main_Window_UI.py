from PyQt6 import QtWidgets, QtGui, QtCore
from .Main_Window_Controller import MainWindowController
from .components import FormSection, MenuBar


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_window_controller = MainWindowController()

        self.init_ui()

    def init_ui(self):
        # Configurar la ventana
        self.setWindowTitle("Graph App")
        self.setGeometry(0, 0, 1200, 750)

        widget = QtWidgets.QWidget()

        # Crear un grid-layout con dos secciones
        layout = QtWidgets.QGridLayout(widget)

        menubar = MenuBar(self.main_window_controller).create_menu_bar()
        button_section = FormSection(self.main_window_controller).create_button_section()
        image_section = self.create_image_section()

        content = QtWidgets.QWidget()
        content_layout = QtWidgets.QGridLayout(content)

        # Añadir la sección de los botones a la parte superior del grid-layout
        content_layout.addWidget(button_section, 0, 1)
        content_layout.addWidget(image_section, 0, 0)

        layout.addWidget(menubar, 0, 0)
        # Añadir la sección de la imagen a la parte inferior del grid-layout
        layout.addWidget(content, 1, 0)

        self.setCentralWidget(widget)

    def create_image_section(self):
        # Crear una sección para mostrar la imagen
        image_tab = QtWidgets.QTabWidget(self)
        image_tab.setStyleSheet('font-size: 18px')
        image_layout = QtWidgets.QVBoxLayout(image_tab)

        for graph_name, graph in self.main_window_controller.graphs.items():
            # Crear un label para mostrar la imagen
            image_label = QtWidgets.QLabel(self)
            image_label.setScaledContents(True)

            # ruta de la imagen (que es igual al nombre del grafo creado)
            image_route = self.main_window_controller.get_graph_image_route(graph_name)

            # mostrar imagen
            pixmap = QtGui.QPixmap(image_route)
            image_label.setPixmap(pixmap)

            image_tab.addTab(image_label, graph_name)

        # Añadir el label a la sección de la imagen
        image_layout.addWidget(image_tab)

        return image_tab

