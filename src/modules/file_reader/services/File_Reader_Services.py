import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from src.modules.graph.classes import Graph, GraphNode, GraphEdge
from src.modules.graph.services import GraphServices
from src.modules.file_reader.constants import GRAPH_IMAGES_PATH,GRAPH_TXT_PATH


class FileReaderServices:
    @staticmethod
    def import_graph(path):
        with open(path, 'r') as file:
            labels = file.readline().split(" ")
            matrix = np.zeros([len(file.readline().split(" ")), len(file.readline().split(" "))])
            i = 0
            for line in file.readlines(3):
                if line.strip():
                    matrix[i] = line.split(" ")
                    i = i + 1
        return GraphServices.matrix_to_graph(matrix, labels)

    @staticmethod
    def import_graph_txt(path):
        matrix = np.loadtxt(path, skiprows=2, dtype=int)
        with open(path, 'r') as file:
            labels = file.readline().split(" ")
        return GraphServices.matrix_to_graph(matrix, labels)

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

    @staticmethod
    def export_graph_to_image(graph: Graph, image_name: str):
        # convertir el grafo normal a un grafo de networkx
        save_graph = FileReaderServices.convert_graph_to_nx_graph(graph)

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

    @staticmethod
    def create_graph_image_route(image_name: str) -> str:
        return f'{GRAPH_IMAGES_PATH}/{image_name}.png'

    @staticmethod
    def create_graph_txt_route(file_name: str) -> str:
        return f'{GRAPH_TXT_PATH}/{file_name}.png'

    @staticmethod
    def convert_graph_to_nx_graph(graph: Graph) -> nx.DiGraph:
        all_graph_nodes: list[GraphNode] = graph.node_list

        save_graph = nx.DiGraph()

        for node in all_graph_nodes:
            node_label = str(node.label)
            save_graph.add_node(node_label)

        for node in all_graph_nodes:
            node_edges: list[GraphEdge] = node.edge_list
            node_label = str(node.label)

            for edge in node_edges:
                next_node_label = str(edge.node.label)
                save_graph.add_edge(node_label, next_node_label, weight=edge.weight)

        return save_graph
