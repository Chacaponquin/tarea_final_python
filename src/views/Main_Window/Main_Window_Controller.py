from src.modules.graph.services import GraphServices
from src.modules.file_reader.services import FileReaderServices
from src.modules.graph.classes import Graph, GraphNode
from .classes import GraphForm
from PyQt6 import QtCore


class Signals(QtCore.QObject):
    updateNodesFormSignal = QtCore.pyqtSignal()


class MainWindowController:
    def __init__(self):
        # signals
        self.signals = Signals()

        # services
        self.graph_services = GraphServices()
        self.file_reader_services = FileReaderServices()

        # lista de todos los grafos utilizados
        self.graphs: dict = {'Init Graph': self.create_default_graph()}

        # índice del grafo seleccionado
        self.selected_graph = 0

        # selected graph form
        self.graph_form = GraphForm(self.get_selected_graph())

        # crear la imagen del grafo creado por defecto
        self.save_graph_image('Init Graph')

    def get_selected_graph(self) -> (str, Graph):
        return list(self.graphs.items())[self.selected_graph]

    # método para guardar uno de los grafos guardados en una imagen
    def save_graph_image(self, graph_name: str):
        save_graph = self.graphs[graph_name]
        self.file_reader_services.export_graph_to_image(save_graph, graph_name)

    def get_graph_image_route(self, graph_name: str) -> str:
        return FileReaderServices.create_graph_image_route(graph_name)

    def add_node_form(self):
        self.graph_form.add_node()
        print(self.graph_form.nodes_form)
        self.signals.updateNodesFormSignal.emit()

    # método para crear el primer grafo que se muestra en la pantalla
    def create_default_graph(self) -> Graph:
        new_graph = Graph()

        node_a = GraphNode('A')
        node_b = GraphNode('B')
        node_c = GraphNode('C')

        # guardar los nodos en el grafo
        nodes = [node_a, node_b, node_c]

        for node in nodes:
            new_graph.add_node(node.label)

        # creando conexiones
        new_graph.connect(node_a.label, node_b.label, 10)
        new_graph.connect(node_a.label, node_c.label, 5)
        new_graph.connect(node_b.label, node_c.label, 2)

        return new_graph

    def import_txts(self, file_routes: list[str]):
        try:
            for file in file_routes:
                new_graph = self.file_reader_services.import_graph_txt(file)
        except:
            print('Error')


