from src.modules.graph.classes.Graph import Graph
import numpy as np

from src.modules.graph.classes.GraphNode import GraphNode


class GraphServices:
    @staticmethod
    def matrix_to_graph(matrix, labels):
        graph = Graph()
        for label in labels:
            graph.add_node(label)
        i = 0
        while i < len(matrix):
            j = 0
            while j < len(matrix[i]):
                if i != j and matrix[i][j] != 0:
                    graph.connect(labels[j], labels[i], matrix[i][j])
                j = j + 1
            i = i + 1
        return graph

    @staticmethod
    def graph_to_matrix(graph):
        matrix = np.zeros([len(graph.node_list), len(graph.node_list)])
        i = 0
        while i < len(graph.node_list):
            j = 0
            while j < len(graph.node_list):
                adjacent_node_edge = graph.node_list[i].get_edge(graph.node_list[j])
                if i != j and adjacent_node_edge is not None:
                    matrix[j][i] = adjacent_node_edge.weight
                j = j + 1
            i = i + 1
        return matrix

