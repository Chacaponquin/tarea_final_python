from src.modules.graph.classes.GraphEdge import GraphEdge
from src.modules.graph.exceptions import EmptyNodeLabelException, ConnectionAlreadyExistsException, NotExistEdge


class GraphNode:
    # label es un string
    def __init__(self, label: str):
        self.label = self.validate_label(label)
        self.edge_list: list[GraphEdge] = []

    def validate_label(self, label) -> str:
        if label == '':
            raise EmptyNodeLabelException()
        else:
            return label

    def __str__(self):
        return self.label

    def __eq__(self, other):
        return other.label == self.label

    # eliminar una arista de la lista de aristas, se recibe el nodo hacia el cual apunta la arista
    def delete_edge(self, node):
        edge = self.get_edge(node)
        if edge is None:
            raise ConnectionAlreadyExistsException(self.label, node.label)
        else:
            self.edge_list.remove(edge)
        return edge is not None

    # Retorna None si no existe arista entre ellos
    def get_edge(self, node):
        edge = None
        i = 0
        found = False
        while i < len(self.edge_list) and not found:
            if self.edge_list[i].node == node:
                edge = self.edge_list[i]
                found = True
            else:
                i = i+1
        return edge

    # retorna TRUE si se puede añadir y retorna FALSE si existe una arista que apunta hacia ese nodo
    def add_edge(self, node, weight: float):
        edge = self.get_edge(node)
        if edge is not None:
            raise ConnectionAlreadyExistsException(self.label, node.label)
        else:
            self.edge_list.append(GraphEdge(node, weight))
        return edge is None

    # retorna TRUE si se pudo modificar el peso
    def change_weight(self, node, new_weight: float):
        result = False
        edge = self.get_edge(node)
        if edge is None:
            raise NotExistEdge(self.label, node.label)
        else:
            result = edge.change_weight(new_weight)
        return result

   ##Retorna False si no son adyacentes
    def is_adjacent(self, node):
        edge = self.get_edge(node)
        return edge is not None

    def get_adjacents_nodes(self):
        adjacents = []
        for edge in self.edge_list:
            adjacents.append(edge.node)
        return adjacents

    def get_adjacents_labels(self):
        adjacents = []
        for edge in self.edge_list:
            adjacents.append(edge.node.label)
        return adjacents


