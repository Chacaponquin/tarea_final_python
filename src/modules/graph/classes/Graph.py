from src.modules.graph.classes.GraphNode import GraphNode
from queue import Queue
from src.modules.graph.exceptions import DuplicateNodeException, NodeConnectToItself, NotExistNode


class Graph:
    def __init__(self):
        self.node_list: list[GraphNode] = []

    def add_node(self, label: str):
        node = self.get_node(label)
        if node is None:
            self.node_list.append(GraphNode(label))
        else:
            raise DuplicateNodeException(label)

        return node is None

    # Retorna un nodo dado un label o None si no existe el nodo
    def get_node(self, label: str) -> GraphNode:
        node = None
        i = 0
        found = False
        while i < len(self.node_list) and not found:
            if self.node_list[i].label == label:
                node = self.node_list[i]
                found = True
            else:
                i = i + 1

        return node

    # Retorna True o False en dependencia de si se pudo eliminar la arista o no
    def delete_node(self, label: str):
        node = self.get_node(label)
        if node is not None:
            for node_n in self.node_list:
                if node_n.is_adjacent(node):
                    node_n.delete_edge(node)
            self.node_list.remove(node)
        else:
            raise NotExistNode(label)

        return node is not None

    # Conecta dos nodos del grafo(Recibe las etiquetas) retorna True o False
    # en dependencia de si fue posible o no conectar los nodos
    def connect(self, label_1: str, label_2: str, weight: float):
        if label_1 == label_2:
            raise NodeConnectToItself(label_1)
        else:
            node_1 = self.get_node(label_1)
            if node_1 is None:
                raise NotExistNode(label_1)
            else:
                node_2 = self.get_node(label_2)
                if node_2 is None:
                    raise NotExistNode(node_2)

        return node_1.add_edge(node_2, weight)

    # Conecta dos nodos del grafo
    def connect_nodes(self, node_1: GraphNode, node_2: GraphNode, weight: float):
        return self.connect(node_1.label, node_2.label, weight)

    # Elimina la arista entre dos nodos(Recibe las etiquetas) retorna True o False
    # en dependencia de si fue posible o no conectar los nodos
    def disconnect(self, label_1: str, label_2:str):
        node_1 = self.get_node(label_1)
        if node_1 is None:
            raise NotExistNode(label_1)
        else:
            node_2 = self.get_node(label_2)
            if node_2 is None:
                raise NotExistNode(label_2)
        return node_1.delete_edge(node_2)

    # Elimina la arista entre dos nodos
    def disconnect_nodes(self, node_1: GraphNode, node_2: GraphNode):
        return self.disconnect(node_1.label, node_2.label)

    # Verifica si dos nodos son adyacentes
    def are_adjacent(self, node_1: GraphNode, node_2:GraphNode):
        return node_1.is_adjacent(node_2)

    def change_weight(self, node_1:GraphNode, node_2:GraphNode, weight: float):
        node_1.change_weight(node_2, weight)

    # Se utiliza una cola para llevar a cabo el recorrido a lo ancho del grafo
    # La cola se inicializa con el nodo de origen, en cada iteración del ciclo while
    # se saca el primer nodo que se encuentra en la cola, se añade a visitados su label y se agregan a la cola
    # los nodos adyacentes no visitados
    # Retorna una lista con las etiquetas de cada nodo del grafo recorrido a lo ancho
    def width_transversal(self, node: GraphNode):
        if node in self.node_list:
            queue = Queue()
            visited = []
            result = []
            queue.put(node)
            while not queue.empty():
                actual_node = queue.get()
                visited.append(actual_node.label)
                if actual_node.label not in result:
                    result.append(actual_node.label)
                adj_nodes = actual_node.get_adjacents_nodes()
                for node_n in adj_nodes:
                    if not visited.__contains__(node_n.label):
                        queue.put(node_n)
        else:
            raise NotExistNode(node.label)

        return result

    # Retorna una lista con las etiquetas de los nodos aislados del grafo
    def isolated_nodes(self):
        nodes: list[str] = []
        for n in self.node_list:
            if not n.edge_list:
                nodes.append(n.label)

        return nodes

    # Retorna una lista con las etiquetas de los nodos que apuntan hacia un nodo pasado por parámetro
    def arrived_nodes(self, node: GraphNode):
        nodes = []
        for n in self.node_list:
            if node.label in n.get_get_adjacents_labels():
                nodes.append(n.label)
        return nodes

    # se utiliza un arreglo para guardar los nodos que se vayan visitando
    # se llama la función recursiva depth_first_search_util
    # la función añade al nodo a la lista visited de no estar ya en ella
    # repite el proceso para todos los nodos adyacentes
    def depth_first_search(self, node: GraphNode):
        visited = []
        if len(node.edge_list) > 0:
            self.depth_first_search_util(node, visited)
        return visited

    def depth_first_search_util(self, node: GraphNode, visited: list[str]):
        if node.label not in visited:
            visited.append(node.label)
        for edge in node.edge_list:
            if edge.node.label not in visited:
                self.depth_first_search_util(edge.node, visited)

