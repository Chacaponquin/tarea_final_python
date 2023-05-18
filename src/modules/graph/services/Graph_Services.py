from src.modules.graph.classes.Graph import Graph
from src.modules.graph.classes.GraphEdge import GraphEdge
from src.modules.graph.classes.GraphNode import GraphNode
from src.modules.graph.exceptions import NodeConnectToItself
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


class GraphServices:
    def get_graph_plot_figure(self, graph: Graph):
        save_graph = self.convert_graph_to_nx_graph(graph)

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
        return plt.figure()

    @staticmethod
    def matrix_to_graph(labels, matrix: list[list[float]]):
        graph = Graph()

        for label in labels:
            graph.add_node(label)

        for row_index, row in enumerate(matrix):
            for column_index, weight in enumerate(row):
                if column_index == row_index:
                    if matrix[row_index][column_index] != 0:
                        raise NodeConnectToItself(labels[column_index])
                else:
                    node_1 = labels[row_index]
                    node_2 = labels[column_index]

                    graph.connect(node_1, node_2, weight)

        return graph

    @staticmethod
    def graph_to_matrix(graph: Graph):
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

    def convert_graph_to_nx_graph(self, graph: Graph) -> nx.DiGraph:
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



