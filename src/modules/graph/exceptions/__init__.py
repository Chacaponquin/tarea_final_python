class EmptyNodeLabelException(TypeError):
    pass


class DuplicateNodeException(Exception):
    def __init__(self, label):
        self.duplicate_label = label
        self.message = f"Ya existe un nodo con el identificador {label} en el grafo"

