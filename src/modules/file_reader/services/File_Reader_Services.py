import re

import numpy as np

from src.modules.graph.classes.Graph import Graph
from src.modules.graph.classes.GraphNode import GraphNode
from src.modules.graph.services import GraphServices


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
    def export_graph(graph, path):
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