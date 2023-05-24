from PyQt6 import QtWidgets, QtGui
from src.views.Main_Window.Main_Window_Controller import MainWindowController


class ImageSection:
    def __init__(self, parent_layout: QtWidgets.QGridLayout, main_window_controller: MainWindowController):
        # parent layout
        self.parent_layout = parent_layout

        self.creating = False

        # controller
        self.main_window_controller = main_window_controller

        # Crear una sección para mostrar la imagen
        self.image_tab = QtWidgets.QTabWidget()
        self.image_tab.setStyleSheet('font-size: 18px')

        self.image_tab.setFixedWidth(1000)

        # añadir accion cuando se cambie la tab
        self.image_tab.currentChanged.connect(self.change_tab_action)

        self.image_layout = QtWidgets.QVBoxLayout(self.image_tab)

        # actualizar los grafos
        self.update_graphs()

        # Añadir el label a la sección de la imagen
        self.image_layout.addWidget(self.image_tab)

        # add to layout
        self.parent_layout.addWidget(self.image_tab, 0, 0)

    def change_tab_action(self, tab_index: int):
        if tab_index >= 0 and not self.creating:
            self.main_window_controller.change_select_graph(tab_index)
            self.image_tab.setCurrentIndex(self.main_window_controller.selected_graph)

    def update_graphs_action(self):
        self.update_graphs()

    def change_tab_index(self, index: int):
        self.image_tab.setCurrentIndex(index)

    def update_graphs(self):
        self.creating = True
        self.image_tab.clear()
        for index, graph in enumerate(self.main_window_controller.graphs):
            # ruta de la imagen (que es igual al nombre del grafo creado)
            image_route = self.main_window_controller.get_graph_image_route(graph['name'])

            # Crear un label para mostrar la imagen
            image_label = QtWidgets.QLabel()

            image_label.setStyleSheet(f'width: 100%; background-image: url("{image_route}"); background-repeat: no-repeat; background-size: cover;')
            # pixmap = QtGui.QPixmap(image_route)
            # image_label.setPixmap(pixmap)
            image_label.setScaledContents(True)

            self.image_tab.addTab(image_label, graph['name'])
        self.creating = False

        self.image_tab.setCurrentIndex(self.main_window_controller.selected_graph)
