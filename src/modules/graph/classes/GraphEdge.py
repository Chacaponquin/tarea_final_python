from src.modules.graph.exceptions import NotAFloat


class GraphEdge:
    # node es el nodo al que va dirigido la arista
    # weight es el peso de la arista (un número)
    def __init__(self, node, weight: float):
        self.node = node
        self.weight = float(weight)

    def __str__(self):
        return str(self.node) + " peso: " + str(self.weight)

    def change_weight(self, new_weight):
        result = False
        if not isinstance(new_weight, float):
            raise NotAFloat(new_weight)
        else:
            self.weight = new_weight
            result = True
        return result



