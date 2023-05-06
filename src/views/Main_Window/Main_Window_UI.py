from PyQt6 import QtWidgets, QtGui, QtCore
from .Main_Window_Controller import MainWindowController


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_window_controller = MainWindowController()

        # índice del grafo seleccionado
        self.selected_graph = 0

        self.init_ui()

    def init_ui(self):
        # Configurar la ventana
        self.setWindowTitle("Graph App")
        self.setGeometry(0, 0, 1200, 750)

        widget = QtWidgets.QWidget()

        # Crear un grid-layout con dos secciones
        layout = QtWidgets.QGridLayout(widget)

        menubar = self.create_menu_bar()
        button_section = self.create_button_section()
        image_section = self.create_image_section()

        content = QtWidgets.QWidget()
        contentLayout = QtWidgets.QGridLayout(content)

        # Añadir la sección de los botones a la parte superior del grid-layout
        contentLayout.addWidget(button_section, 0, 1)
        contentLayout.addWidget(image_section, 0, 0)

        layout.addWidget(menubar, 0, 0)
        # Añadir la sección de la imagen a la parte inferior del grid-layout
        layout.addWidget(content, 1, 0)

        self.setCentralWidget(widget)

    def create_menu_bar(self):
        # create menu
        menubar = QtWidgets.QMenuBar()
        menubar.setFixedHeight(50)
        actionFile = menubar.addMenu("File")
        actionFile.addAction("New")
        actionFile.addAction("Open")
        actionFile.addAction("Save")
        actionFile.addSeparator()
        actionFile.addAction("Quit")

        return menubar

    def create_image_section(self):
        # Crear una sección para mostrar la imagen
        image_tab = QtWidgets.QTabWidget(self)
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

    def create_button_section(self):
        # Crear una sección para los botones
        button_section = QtWidgets.QWidget(self)
        button_section.setMaximumWidth(300)
        button_section.setStyleSheet('background-color: white;')

        button_layout = QtWidgets.QVBoxLayout(button_section)

        add_button_widget = QtWidgets.QWidget()
        add_button_layout = QtWidgets.QHBoxLayout(add_button_widget)
        add_button_layout.addStretch()

        add_node_button = QtWidgets.QPushButton('Add Node')
        add_node_button.setFixedWidth(100)
        add_node_button.setStyleSheet('background-color: green; color: white; font-weight: 600')
        add_button_layout.addWidget(add_node_button)

        add_button_widget.setLayout(add_button_layout)

        nodes_title = QtWidgets.QLabel()
        nodes_title.setText('Nodes')
        nodes_title.setStyleSheet('font-size: 22px; font-weight: 700')

        nodes_section = QtWidgets.QWidget()
        nodes_section_layout = QtWidgets.QVBoxLayout()
        nodes_section.setLayout(nodes_section_layout)

        # buscar el grafo seleccionado
        selected_graph_name, selected_graph = self.main_window_controller.get_graph_by_index(self.selected_graph)

        for node in selected_graph.node_list:
            node_config_section = QtWidgets.QWidget()
            node_config_layout = QtWidgets.QHBoxLayout()
            node_config_section.setLayout(node_config_layout)

            # node name input
            node_name_edit = QtWidgets.QLineEdit()
            node_name_edit.setFixedWidth(50)
            node_name_edit.setText(node.label)

            # node connection input
            node_connection_edit = QtWidgets.QLineEdit()
            connections_list = self.main_window_controller.get_node_connections_string(node)
            node_connection_edit.setText(connections_list)

            node_config_layout.addWidget(node_name_edit)
            node_config_layout.addWidget(node_connection_edit)

            nodes_section_layout.addWidget(node_config_section)

        button_layout.addWidget(nodes_title)
        button_layout.addWidget(nodes_section)
        button_layout.addWidget(add_button_widget)
        button_layout.addStretch()

        return button_section

    def load_image(self):
        # Abrir un cuadro de diálogo para seleccionar una imagen
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Abrir imagen", QtCore.QDir.homePath())

        if file_name:
            # Cargar la imagen seleccionada y mostrarla en el label
            pixmap = QtGui.QPixmap(file_name)
            self.image_label.setPixmap(pixmap)