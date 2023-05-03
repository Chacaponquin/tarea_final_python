from src.modules.graph.classes.GraphNode import GraphNode
from queue import Queue


class Graph:
    def __init__(self):
        self.node_list = []

    def add_node(self, label):
        node = self.get_node(label)
        if node is None:
            self.node_list.append(GraphNode(label))
        return node is None

    #Devuelve un nodo del grafo dado una etiqueta
    def get_node(self, label):
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

    def delete_node(self, label):
        node = self.get_node(label)
        if node is not None:
            for node_n in self.node_list:
                if node_n.is_adjacent(node):
                    node_n.delete_edge(node)
            self.node_list.remove(node)
        return node is not None

    ##Conecta dos nodos del grafo(Recibe las etiquetas)
    def connect(self, label_1, label_2, weight):
        node_1 = self.get_node(label_1)
        node_2 = self.get_node(label_2)
        return node_1.add_edge(node_2, weight)

    #Conecta dos nodos del grafo
    def connect_nodes(self, node_1, node_2, weight):
        return self.connect(node_1.label, node_2.label, weight)

    # Elimina la arista entre dos nodos(Recibe las etiquetas)
    def disconnect(self, label_1, label_2):
        node_1 = self.get_node(label_1)
        node_2 = self.get_node(label_2)
        return node_1.delete_edge(node_2)

    #Elimina la arista entre dos nodos
    def disconnect_nodes(self, node_1, node_2):
        return self.disconnect(node_1.label, node_2.label)

    #Verifica si dos nodos son adyacentes
    def are_adjacent(self, node_1, node_2):
        return node_1.is_adjacent(node_2)

    # Se utiliza una cola para llevar a cabo el recorrido a lo ancho del grafo
    # La cola se inicializa con el nodo de origen, en cada iteración del ciclo while
    # se saca el primer nodo que se encuentra en la cola, se añade a visitados su label y se agregan a la cola
    # los nodos adyacentes no visitados
    # Retorna una lista con las etiquetas de cada nodo del grafo recorrido a lo ancho

    def bfs(self, node):
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
        return result


    #Retorna una lista con las etiquetas de los nodos aislados del grafo
    def isolated_nodes(self):
        nodes = []
        for n in self.node_list:
            if not n.edge_list:
                  nodes.append(n.label)
        return nodes

    #Retorna una lista con las etiquetas de los nodos que apuntan hacia un nodo pasado por párametro
    def arrived_nodes(self,node):
        nodes = []
        for n in self.node_list:
            if node.label in n.get_get_adjacents_labels():
                nodes.append(n.label)
        return nodes



