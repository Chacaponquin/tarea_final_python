from src.modules.graph.services import GraphServices
from src.modules.file_reader.services import FileReaderServices
from src.modules.graph.classes import Graph, GraphNode


class MainWindowController:
    def __init__(self):
        self.graph_services = GraphServices()
        self.file_reader_services = FileReaderServices()

        # lista de todos los grafos utilizados
        self.graphs: dict = {'Init Graph': self.create_default_graph()}

        # crear la imagen del grafo creado por defecto
        self.save_graph_image('Init Graph')

    def get_graph_by_index(self, index: int) -> (str, Graph):
        return list(self.graphs.items())[index]

    def get_node_connections_string(self, node: GraphNode) -> str:
        labels_list: list[str] = list(map(lambda n: n.label, node.get_adjacents_nodes()))

        return ', '.join(labels_list)

    # método para guardar uno de los grafos guardados en una imagen
    def save_graph_image(self, graph_name: str):
        save_graph = self.graphs[graph_name]
        self.file_reader_services.export_graph_to_image(save_graph, graph_name)

    def get_graph_image_route(self, graph_name: str) -> str:
        return FileReaderServices.create_graph_image_route(graph_name)

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


