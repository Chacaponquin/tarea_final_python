from src.modules.graph.services import GraphServices
from src.modules.file_reader.services import FileReaderServices
from src.modules.graph.classes import Graph, GraphNode
from .classes import GraphForm
from PyQt6 import QtCore


class Signals(QtCore.QObject):
    updateGraphsSignal = QtCore.pyqtSignal()


class MainWindowController:
    def __init__(self):
        # signals
        self.signals = Signals()

        # services
        self.graph_services = GraphServices()
        self.file_reader_services = FileReaderServices()

        # lista de todos los grafos utilizados
        self.graphs: list[dict] = [{'name': 'Init Graph', 'graph': self.create_default_graph()}]

        # índice del grafo seleccionado
        self.selected_graph = 0

        # selected graph form
        self.graph_form = GraphForm(self.get_selected_graph())

        # crear la imagen de todos los grafos (al principio solo hay uno)
        self.save_all_graphs()

    def update_edge_weight(self, node_index: int, edge_index: int, new_weight: float):
        self.graph_form.update_edge_weight(node_index, edge_index, new_weight)

    def update_edge_name(self, node_index: int, edge_index: int, edge_node_name: str):
        self.graph_form.update_edge_name(node_index, edge_index, edge_node_name)

    def save_all_graphs(self):
        for graph in self.graphs:
            self.save_graph_image(graph['name'])

    def add_node_edge(self, node_index: int):
        self.graph_form.add_node_edge(node_index)

    def get_selected_graph(self) -> (str, Graph):
        graph_inf = self.graphs[self.selected_graph]
        return graph_inf['name'], graph_inf['graph']

    # método para guardar uno de los grafos guardados en una imagen
    def save_graph_image(self, graph_name: str):
        for graph in self.graphs:
            if graph['name'] == graph_name:
                self.file_reader_services.export_graph_to_image(graph['graph'], graph_name)

    def get_graph_image_route(self, graph_name: str) -> str:
        return FileReaderServices.create_graph_image_route(graph_name)

    def add_node_form(self):
        self.graph_form.add_node()

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
                print(new_graph)
        except:
            print('Error')

    def add_new_graph(self):
        self.graphs.append({'name': f'New Graph{len(self.graphs) + 1}', 'graph': self.create_default_graph()})
        self.save_all_graphs()
        # self.signals.updateGraphsSignal.emit()
        print(self.graphs)


