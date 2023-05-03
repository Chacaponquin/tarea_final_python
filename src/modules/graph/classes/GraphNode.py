from src.modules.graph.classes.GraphEdge import GraphEdge

class GraphNode:
    ##label es un string
    def __init__(self, label):
        self.label = label
        self.edge_list = []

    def __str__(self):
        return self.label

    def __eq__(self, other):
        return other.label == self.label

    ##eliminar una arista de la lista de aristas, se recibe el nodo hacia el cual apunta la arista
    def delete_edge(self, node):
        edge = self.get_edge(node)
        if edge is not None:
            self.edge_list.remove(edge)
        return edge is not None

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

    ##retorna TRUE si se puede añadir y retorna FALSE si existe una arista que apunta hacia ese nodo
    def add_edge(self, node, weight):
        edge = self.get_edge(node)
        result = edge is None
        if result:
            self.edge_list.append(GraphEdge(node, weight))
        return result

    def change_weight(self, node, new_weight):
        i = 0
        found = False
        while i < len(self.edge_list) and not found:
            if self.edge_list[i].node == node:
                self.edge_list[i].weight = new_weight
                found = True
            else:
                i = i + 1
        return found

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


