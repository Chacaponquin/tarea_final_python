from PyQt6 import QtWidgets
from src.views.Main_Window.Main_Window_Controller import MainWindowController
from src.views.Main_Window.classes.GraphForm import GraphForm


class FormSection:
    def __init__(self, main_window_controller: MainWindowController):
        # controller
        self.main_window_controller = main_window_controller

        # añadir signal
        self.main_window_controller.signals.updateNodesFormSignal.connect(lambda x: self.updateSection())

        # create section
        self.button_section = QtWidgets.QWidget()
        self.button_layout = QtWidgets.QVBoxLayout(self.button_section)

        # actualizar la sección con los datos
        self.updateSection()

    def create_button_section(self):
        return self.button_section

    def updateSection(self):
        self.button_section = QtWidgets.QWidget()
        self.button_section.setMaximumWidth(300)
        self.button_section.setStyleSheet('background-color: white;')

        # create layout
        self.button_layout = QtWidgets.QVBoxLayout(self.button_section)

        # pintar el header
        self.paint_form_title_section()

        # pintar el formulario de nodos
        self.paint_node_form()

        # sección de botones actualizar y añadir
        self.paint_buttons_section()

        self.button_layout.addStretch()

        self.button_section.setLayout(self.button_layout)

    def paint_form_title_section(self):
        nodes_title = QtWidgets.QLabel()
        nodes_title.setText('Nodes')
        nodes_title.setStyleSheet('font-size: 22px; font-weight: 700')

        self.button_layout.addWidget(nodes_title)

    def paint_buttons_section(self):
        add_button_widget = QtWidgets.QWidget()
        add_button_layout = QtWidgets.QHBoxLayout(add_button_widget)
        add_button_layout.addStretch()

        add_node_button = QtWidgets.QPushButton('Add Node')
        add_node_button.setFixedWidth(100)
        add_node_button.setStyleSheet('background-color: green; color: white; font-weight: 600')
        add_node_button.clicked.connect(self.main_window_controller.add_node_form)

        update_node_button = QtWidgets.QPushButton('Update')
        update_node_button.setFixedWidth(100)
        update_node_button.setStyleSheet('background-color: blue; color: white; font-weight: 600')

        add_button_layout.addWidget(update_node_button)
        add_button_layout.addWidget(add_node_button)

        add_button_widget.setLayout(add_button_layout)

        self.button_layout.addWidget(add_button_widget)

    def paint_node_form(self):
        nodes_section = QtWidgets.QWidget()
        nodes_section_layout = QtWidgets.QVBoxLayout()
        nodes_section.setLayout(nodes_section_layout)

        # buscar el grafo seleccionado
        selected_graph_form = self.main_window_controller.graph_form

        for node_index, node_inf in enumerate(selected_graph_form.nodes_form):
            node_name, node_connections = node_inf
            node_config_section = self.create_node_form_section(node_index, node_name, node_connections, selected_graph_form)
            nodes_section_layout.addWidget(node_config_section)

        # add to layout
        self.button_layout.addWidget(nodes_section)

    def create_node_form_section(self, index: int, node_name: str, node_connections: list[str], graph_form: GraphForm):
        node_config_section = QtWidgets.QWidget()
        node_config_layout = QtWidgets.QHBoxLayout()
        node_config_section.setLayout(node_config_layout)

        def change_node_name(name: str):
            graph_form.update_node_name(index, name)

        def change_node_connection(connections: str):
            graph_form.update_node_connections(index, connections)

        # node name input
        node_name_edit = QtWidgets.QLineEdit()
        node_name_edit.setFixedWidth(50)
        node_name_edit.setText(node_name)
        node_name_edit.textChanged.connect(lambda n: change_node_name(n))

        # node connection input
        node_connection_edit = QtWidgets.QLineEdit()
        node_connection_edit.setText(node_connections)
        node_connection_edit.textChanged.connect(lambda n: change_node_connection(n))

        node_config_layout.addWidget(node_name_edit)
        node_config_layout.addWidget(node_connection_edit)

        return node_config_section
