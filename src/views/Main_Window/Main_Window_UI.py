from PyQt6 import QtWidgets, QtGui, QtCore
from .Main_Window_Controller import MainWindowController


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
        image_section = QtWidgets.QWidget(self)
        image_layout = QtWidgets.QVBoxLayout(image_section)

        # Crear un label para mostrar la imagen
        image_label = QtWidgets.QLabel(self)
        image_label.setScaledContents(True)
        pixmap = QtGui.QPixmap(self.main_window_controller.get_graph_image_route('test'))
        image_label.setPixmap(pixmap)

        # Añadir el label a la sección de la imagen
        image_layout.addWidget(image_label)

        self.main_window_controller.save_graph_image()

        return image_section

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

        button_layout.addWidget(add_button_widget)

        nodes_title = QtWidgets.QLabel()
        nodes_title.setText('Nodes')
        nodes_title.setStyleSheet('font-size: 22px; font-weight: 700')

        button_layout.addWidget(nodes_title)

        button_layout.addStretch()

        return button_section

    def load_image(self):
        # Abrir un cuadro de diálogo para seleccionar una imagen
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Abrir imagen", QtCore.QDir.homePath())

        if file_name:
            # Cargar la imagen seleccionada y mostrarla en el label
            pixmap = QtGui.QPixmap(file_name)
            self.image_label.setPixmap(pixmap)