
import networkx as nx
import matplotlib.pyplot as plt

from src.modules.file_reader.exceptions import EmptyFileError, FileFormattingError
from src.modules.graph.classes import Graph, GraphNode, GraphEdge
from src.modules.graph.services import GraphServices
from src.modules.graph.exceptions import DuplicateNodeException
from src.modules.file_reader.constants import GRAPH_IMAGES_PATH,GRAPH_TXT_PATH


class FileReaderServices:
    def __init__(self):
        self.graph_services = GraphServices()

    @staticmethod
    def import_graph(path):
        with open(path, 'r') as file:
            file_content: list[str] = file.read().split('\n')

            nodes_names: list[str] = []

            try:
                nodes_names = file_content[0].split(' ')
                weight_matrix: list[list[float]] = [[0 for i in range(len(nodes_names))] for i in
                                                    range(len(nodes_names))]
            except IndexError:
                raise FileFormattingError(f'La primera fila del archivo deben ser los nombres de los nodos.')

            try:
                if file_content[1] == '':
                    weight_content = file_content[2:]

                    i = 0
                    while i < len(weight_content) and i < len(nodes_names):
                        line = weight_content[i]
                        row_line_weights = line.split(' ')

                        j = 0
                        while j < len(line) and j < len(row_line_weights):
                            w = row_line_weights[j]
                            if w.isnumeric():
                                weight_matrix[i][j] = float(w)
                            else:
                                raise FileFormattingError(f'La conexión entre los nodos debe ser un número. {w} no es un número')

                            j += 1

                        i += 1
                else:
                    raise FileFormattingError(f'Se debe dejar un espacio en blanco para definir la matriz de pesos')
            except IndexError:
                raise FileFormattingError(f'Se debe dejar un espacio en blanco para definir la matriz de pesos')

        try:
            return_graph = GraphServices.matrix_to_graph(nodes_names, weight_matrix)
        except DuplicateNodeException as error:
            raise FileFormattingError(f'Existe el nodo {error.duplicate_label} duplicado')
        except Exception as error:
            raise FileFormattingError('Hubo un error')

        return return_graph

    @staticmethod
    def export_graph(graph: Graph, path):
        matrix = GraphServices.graph_to_matrix(graph)
        labels = []
        for node in graph.node_list:
            labels.append(node.label)
        with open(path, 'w') as file:
            file.write(" ".join(labels) + "\n\n")
            for row in matrix:
                str_row = str(row).replace("]", "")
                str_row = str_row.replace("[", "")
                str_row = str_row.replace(".", "")
                file.write("".join(str_row) + "\n")

    def export_graph_to_image(self, graph: Graph, image_name: str):
        # convertir el grafo normal a un grafo de networkx
        save_graph = self.graph_services.convert_graph_to_nx_graph(graph)

        # crear la ruta de la imagen a exportar
        image_route = FileReaderServices.create_graph_image_route(image_name)

        graph_edges = [(u, v) for (u, v, d) in save_graph.edges(data=True)]

        # positions for all nodes - seed for reproducibility
        pos = nx.spring_layout(save_graph, seed=20)

        # nodes
        nx.draw_networkx_nodes(save_graph, pos, node_size=500)

        # edges
        nx.draw_networkx_edges(save_graph, pos, edgelist=graph_edges, width=2)

        # node labels
        nx.draw_networkx_labels(save_graph, pos, font_size=15)
        # edge weight labels
        edge_labels = nx.get_edge_attributes(save_graph, "weight")
        nx.draw_networkx_edge_labels(save_graph, pos, edge_labels)

        # guardar imagen con matplotlib
        plt.axis("off")
        plt.savefig(image_route)
        plt.close()

    @staticmethod
    def create_graph_image_route(image_name: str) -> str:
        return f'{GRAPH_IMAGES_PATH}/{image_name}.png'

    @staticmethod
    def create_graph_txt_route(file_name: str) -> str:
        return f'{GRAPH_TXT_PATH}/{file_name}.png'



