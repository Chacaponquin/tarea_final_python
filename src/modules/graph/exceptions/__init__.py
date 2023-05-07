class EmptyNodeLabelException(TypeError):
    pass


class DuplicateNodeException(Exception):
    def __init__(self, label):
        self.duplicate_label = label
        self.message = f"Ya existe un nodo con el identificador {label} en el grafo"


class NodeConnectToItself(Exception):
    def __init__(self, node_label: str):
        self.message = f'El nodo {node_label} no se puede conectar consigo mismo'
        self.node_label = node_label
