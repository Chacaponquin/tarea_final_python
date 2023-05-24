class EmptyNodeLabelException(TypeError):
    pass


class DuplicateNodeException(Exception):
    def __init__(self, label):
        self.duplicate_label = label
        self.message = f"Ya existe un nodo con el identificador {label} en el grafo"
        super().__init__(self.message)


class NodeConnectToItself(Exception):
    def __init__(self, node_label: str):
        self.message = f'El nodo {node_label} no se puede conectar consigo mismo'
        self.node_label = node_label
        super().__init__(self.message)


class ConnectionAlreadyExistsException(Exception):
    def __init__(self, node_1: str, node_2: str):
        self.message = f'Ya existe una arista entre {node_1} y {node_2}'
        self.node_1 = node_1
        self.node_2 = node_2
        super().__init__(self.message)


class NotExistNode(Exception):
    def __init__(self, label: str):
        self.message = f'No existe el nodo {label} en el grafo'
        self.label = label
        super().__init__(self.message)


class NotAFloat(Exception):
    def __init__(self, label):
        self.message = 'El peso de las aristas debe ser un número'
        self.label = label
        super().__init__(self.message)


class NotExistEdge(Exception):
    def __init__(self, label_1: str, label_2: str):
        self.message = f'No existe arista entre los nodos {label_1} y {label_2}'
        self.label_1 = label_1
        self.label_2 = label_2
        super().__init__(self.message)

