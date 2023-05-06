from PyQt6 import QtWidgets
from src.views.Main_Window.Main_Window_Controller import MainWindowController
from src.views.Main_Window.classes.GraphForm import GraphForm


def create_button_section(main_window_controller: MainWindowController):
    # Crear una sección para los botones
    button_section = QtWidgets.QWidget()
    button_section.setMaximumWidth(300)
    button_section.setStyleSheet('background-color: white;')

    button_layout = QtWidgets.QVBoxLayout(button_section)

    add_button_widget = QtWidgets.QWidget()
    add_button_layout = QtWidgets.QHBoxLayout(add_button_widget)
    add_button_layout.addStretch()

    add_node_button = QtWidgets.QPushButton('Add Node')
    add_node_button.setFixedWidth(100)
    add_node_button.setStyleSheet('background-color: green; color: white; font-weight: 600')

    update_node_button = QtWidgets.QPushButton('Update')
    update_node_button.setFixedWidth(100)
    update_node_button.setStyleSheet('background-color: blue; color: white; font-weight: 600')

    add_button_layout.addWidget(update_node_button)
    add_button_layout.addWidget(add_node_button)

    add_button_widget.setLayout(add_button_layout)

    nodes_title = QtWidgets.QLabel()
    nodes_title.setText('Nodes')
    nodes_title.setStyleSheet('font-size: 22px; font-weight: 700')

    nodes_section = QtWidgets.QWidget()
    nodes_section_layout = QtWidgets.QVBoxLayout()
    nodes_section.setLayout(nodes_section_layout)

    # pintar el formulario de nodos
    paint_node_form(nodes_section_layout, main_window_controller)

    button_layout.addWidget(nodes_title)
    button_layout.addWidget(nodes_section)
    button_layout.addWidget(add_button_widget)
    button_layout.addStretch()

    return button_section


def paint_node_form(nodes_section_layout, main_window_controller: MainWindowController):
    # buscar el grafo seleccionado
    selected_graph_form = main_window_controller.graph_form

    for node_index, node_inf in enumerate(selected_graph_form.nodes_form):
        node_name, node_connections = node_inf
        node_config_section = create_node_form_section(node_index, node_name, node_connections, selected_graph_form)
        nodes_section_layout.addWidget(node_config_section)


def create_node_form_section(index: int, node_name: str, node_connections: list[str], graph_form: GraphForm):
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
