from PyQt6 import QtWidgets, QtCore, QtGui
from src.views.Main_Window.Main_Window_Controller import MainWindowController
from src.views.Main_Window.classes.GraphForm import GraphForm
from src.modules.graph.exceptions import EmptyNodeLabelException, DuplicateNodeException,NodeConnectToItself, ConnectionAlreadyExistsException, NotExistEdge, NotExistNode, NotAFloat


class FormSection:
    def __init__(self, parent_layout: QtWidgets.QGridLayout, main_window_controller: MainWindowController):
        # parent layout
        self.parent_layout = parent_layout

        # controller
        self.main_window_controller = main_window_controller

        # container
        self.container = QtWidgets.QWidget()

        # create section
        self.button_section = QtWidgets.QWidget()
        self.button_layout = QtWidgets.QVBoxLayout(self.button_section)
        self.button_section.setLayout(self.button_layout)

        self.container_layout = QtWidgets.QVBoxLayout(self.container)
        self.container.setLayout(self.container_layout)

        # actualizar la sección con los datos
        self.update_section()

    def update_scroll(self):
        # container
        self.container = QtWidgets.QWidget()

        # Scroll Area Properties
        scroll = QtWidgets.QScrollArea(self.container)
        scroll.setWidgetResizable(True)
        scroll.setWidget(self.button_section)
        scroll.setFixedHeight(500)
        scroll.setFixedWidth(400)

        #   Scroll Area Layer add
        scroll_layout = QtWidgets.QVBoxLayout()
        scroll_layout.addWidget(scroll)
        scroll_layout.setContentsMargins(0, 0, 0, 0)

        self.container_layout = QtWidgets.QVBoxLayout(self.container)
        self.container_layout.addWidget(scroll)
        self.container.setLayout(self.container_layout)

    def update_section(self):
        # form section
        self.button_section = QtWidgets.QWidget()
        self.button_layout = QtWidgets.QVBoxLayout(self.button_section)

        # pintar el formulario de nodos
        self.paint_node_form()

        # sección de botones actualizar y añadir
        self.paint_buttons_section()

        # añadir espaciado
        self.button_layout.addStretch()

        # añadir botones de exportar y de recorrido
        self.create_options_buttons()

        self.update_scroll()
        self.button_section.setLayout(self.button_layout)
        self.parent_layout.addWidget(self.container, 0, 1)

    def create_options_buttons(self):
        def export_graph_action():
            try:
                # selecting file path
                file_path, _ = QtWidgets.QFileDialog.get(self.button_section, "Save Image", "Graph", "TEXT(*.txt); ")
                print(file_path)
            except Exception as error:
                print(error)

        def width_traversal_action():
            try:
                self.update_graph_action()
                traversal = self.main_window_controller.width_traversal()
                message = f'El recorrido a lo ancho del grafo es {", ".join(traversal)}'
                QtWidgets.QMessageBox.about(self.button_section, 'Recorrido a lo ancho', message)
            except Exception as error:
                QtWidgets.QMessageBox.critical(self.button_section, 'Error', str(error))

        def depht_traversal_action():
            pass

        options_buttons_section = QtWidgets.QWidget()
        options_buttons_layout = QtWidgets.QVBoxLayout(options_buttons_section)

        export_button = QtWidgets.QPushButton('Exportar')
        export_button.clicked.connect(lambda x: export_graph_action())
        export_button.setStyleSheet('font-size: 16px')

        r_a_button = QtWidgets.QPushButton('Recorrido a lo ancho')
        r_a_button.setStyleSheet('font-size: 16px')
        r_a_button.clicked.connect(lambda x: width_traversal_action())

        r_pf_button = QtWidgets.QPushButton('Recorrido en profundidad')
        r_pf_button.setStyleSheet('font-size: 16px')
        r_pf_button.clicked.connect(lambda x: depht_traversal_action())

        options_buttons_layout.addWidget(r_a_button)
        options_buttons_layout.addWidget(r_pf_button)
        options_buttons_layout.addWidget(export_button)

        self.button_layout.addWidget(options_buttons_section)

    def paint_buttons_section(self):
        add_button_widget = QtWidgets.QWidget()
        add_button_layout = QtWidgets.QHBoxLayout(add_button_widget)
        add_button_layout.addStretch()

        add_node_button = QtWidgets.QPushButton('Nuevo Nodo')
        add_node_button.clicked.connect(self.add_node_action)

        update_node_button = QtWidgets.QPushButton('Actualizar')
        update_node_button.clicked.connect(self.update_graph_action)

        add_button_layout.addWidget(update_node_button)
        add_button_layout.addWidget(add_node_button)

        add_button_widget.setLayout(add_button_layout)

        self.button_layout.addWidget(add_button_widget)

    def update_graph_action(self):
        try:
            self.main_window_controller.update_graph_form()
        except EmptyNodeLabelException:
            QtWidgets.QMessageBox.critical(self.button_section, 'Error', 'No pueden existir nodos sin nombre.')
        except DuplicateNodeException as error:
            QtWidgets.QMessageBox.critical(self.button_section, 'Error', f'Existen dos nodos con el nombre {error.duplicate_label}')
        except NodeConnectToItself as error:
            QtWidgets.QMessageBox.critical(self.button_section, 'Error',
                                           f'El nodo {error.node_label} no se puede conectar consigo mismo.')
        except ConnectionAlreadyExistsException as error:
            QtWidgets.QMessageBox.critical(self.button_section, 'Error', error.message)
        except NotExistEdge as error:
            QtWidgets.QMessageBox.critical(self.button_section, 'Error', error.message)
        except NotExistEdge as error:
            QtWidgets.QMessageBox.critical(self.button_section, 'Error', error.message)
        except NotAFloat as error:
            QtWidgets.QMessageBox.critical(self.button_section, 'Error', error.message)
        except Exception as err:
            print(err)

    def add_node_action(self):
        self.main_window_controller.add_node_form()
        self.update_section()

    def paint_node_form(self):
        nodes_section = QtWidgets.QWidget()
        nodes_section_layout = QtWidgets.QVBoxLayout()
        nodes_section_layout.setContentsMargins(0, 0, 0, 0)
        nodes_section.setLayout(nodes_section_layout)

        # buscar el grafo seleccionado
        selected_graph_form = self.main_window_controller.graph_form

        for node_index, node_inf in enumerate(selected_graph_form.nodes_form):
            node_name, node_connections = node_inf
            node_config_section = self.create_node_form_section(node_index, node_name, node_connections, selected_graph_form)
            nodes_section_layout.addWidget(node_config_section)

        # add to layout
        self.button_layout.addWidget(nodes_section)

    def create_node_form_section(self, node_index: int, node_name: str, node_connections: list[(str, float)], graph_form: GraphForm):
        node_config_section = QtWidgets.QWidget()
        node_config_layout = QtWidgets.QGridLayout(node_config_section)
        node_config_layout.setSpacing(0)
        node_config_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        def change_node_name(name: str):
            graph_form.update_node_name(node_index, name)
            self.update_section()

        def add_edge():
            self.main_window_controller.add_node_edge(node_index)
            self.update_section()

        def delete_node():
            self.main_window_controller.delete_node(node_index)
            self.update_section()

        # node name input
        node_name_edit = QtWidgets.QLineEdit()
        node_name_edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        node_name_edit.setFixedWidth(50)
        node_name_edit.setText(node_name)
        node_name_edit.textChanged.connect(lambda n: change_node_name(n))

        for connection_index, connection in enumerate(node_connections):
            edge_node_con, edge_weight = connection
            connection_section = self.create_node_connections(node_index, connection_index, edge_node_con, edge_weight)
            node_config_layout.addWidget(connection_section, connection_index, 1)

        # botones de añadir edge
        add_edge_section = QtWidgets.QWidget()
        node_buttos_layout = QtWidgets.QHBoxLayout(add_edge_section)

        # botón
        node_buttos_layout.addStretch()
        add_edge_button = QtWidgets.QPushButton('Nueva Arista')
        add_edge_button.clicked.connect(lambda x: add_edge())
        node_buttos_layout.addWidget(add_edge_button)

        # delete button
        delete_node_button = QtWidgets.QPushButton('Eliminar Nodo')
        delete_node_button.clicked.connect(lambda x: delete_node())
        delete_node_button.setProperty('class', 'danger')
        node_buttos_layout.addWidget(delete_node_button)

        node_config_layout.addWidget(add_edge_section, len(node_connections), 1)
        node_config_layout.addWidget(node_name_edit, 0, 0)

        return node_config_section

    def create_node_connections(self, node_index, edge_index, edge_node_con, edge_weight):
        def update_edge_weight(new_weight):
            n = '0' if new_weight == '' else new_weight
            self.main_window_controller.update_edge_weight(node_index, edge_index, float(n))

        def delete_edge():
            self.main_window_controller.delete_edge(node_index, edge_index)
            self.update_section()

        connection_section = QtWidgets.QWidget()
        connection_section_layout = QtWidgets.QHBoxLayout(connection_section)

        node_to_connect_input = self.create_node_edge_posible_connections(node_index, edge_index, edge_node_con)

        edge_weight_input = QtWidgets.QLineEdit()
        edge_weight_input.setValidator(QtGui.QDoubleValidator())
        edge_weight_input.setText(str(edge_weight))
        edge_weight_input.textChanged.connect(lambda v: update_edge_weight(v))

        edge_delete_button = QtWidgets.QPushButton("X")
        edge_delete_button.setFixedWidth(30)
        edge_delete_button.setProperty('class', 'danger')
        edge_delete_button.clicked.connect(lambda x: delete_edge())

        connection_section_layout.addWidget(node_to_connect_input)
        connection_section_layout.addWidget(edge_weight_input)
        connection_section_layout.addWidget(edge_delete_button)

        return connection_section

    def create_node_edge_posible_connections(self, node_index: int, edge_index: int, edge_node_con: str):
        def update_edge_node_connector(edge_node_name: str):
            self.main_window_controller.update_edge_name(node_index, edge_index, edge_node_name)

        posible_connections = self.main_window_controller.get_node_posible_connections()

        node_to_connect_input = QtWidgets.QComboBox()

        for p_con in posible_connections:
            node_to_connect_input.addItem(p_con)

        node_to_connect_input.setCurrentText(edge_node_con)

        node_to_connect_input.currentTextChanged.connect(lambda v: update_edge_node_connector(v))

        return node_to_connect_input
