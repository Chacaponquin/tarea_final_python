
class GraphEdge:
    ##node es el nodo al que va dirigido la arista
    ##weight es el peso de la arista (un número)
    def __init__(self, node, weight):
        self.node = node
        self.weight = weight

    def __str__(self):
        return str(self.node) + " peso: " + str(self.weight)


