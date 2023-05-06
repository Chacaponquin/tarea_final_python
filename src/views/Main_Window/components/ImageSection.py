from PyQt6 import QtWidgets, QtGui
from src.views.Main_Window.Main_Window_Controller import MainWindowController


class ImageSection:
    def __init__(self, parent_layout: QtWidgets.QGridLayout, main_window_controller: MainWindowController):
        # parent layout
        self.parent_layout = parent_layout

        # controller
        self.main_window_controller = main_window_controller

        # Crear una sección para mostrar la imagen
        image_tab = QtWidgets.QTabWidget()
        image_tab.setStyleSheet('font-size: 18px')
        image_layout = QtWidgets.QVBoxLayout(image_tab)

        for graph_name, graph in self.main_window_controller.graphs.items():
            # Crear un label para mostrar la imagen
            image_label = QtWidgets.QLabel()
            image_label.setScaledContents(True)

            # ruta de la imagen (que es igual al nombre del grafo creado)
            image_route = self.main_window_controller.get_graph_image_route(graph_name)

            # mostrar imagen
            pixmap = QtGui.QPixmap(image_route)
            image_label.setPixmap(pixmap)

            image_tab.addTab(image_label, graph_name)

        # Añadir el label a la sección de la imagen
        image_layout.addWidget(image_tab)

        # add to layout
        self.parent_layout.addWidget(image_tab, 0, 0)
