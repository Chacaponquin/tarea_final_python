from src.modules.graph.classes import GraphNode, Graph


class GraphForm:
    def __init__(self, selected_graph: Graph):
        self.selected_graph = selected_graph

        self.graph_name: str = ''
        self.nodes_form: list[(str, [(str, float)])] = []

        self.update_form(self.selected_graph)

    def update_node_name(self, node_index: int, new_node_name: str):
        new_form: list[(str, (str, float))] = []

        for node_i, node_inf in enumerate(self.nodes_form):
            if node_index == node_i:
                _, connections = node_inf
                new_form.append((new_node_name, connections))
            else:
                new_form.append(node_inf)

        self.nodes_form = new_form

    def update_node_connections(self, node_index: int, new_connections: (str, float)):
        new_form: list[(str, [(str, float)])] = []

        for node_i, node_inf in enumerate(self.nodes_form):
            if node_index == node_i:
                node_name, _ = node_inf
                new_form.append((node_name, new_connections))
            else:
                new_form.append(node_inf)

        self.nodes_form = new_form

    def update_edge_weight(self, node_index: int, edge_index: int, new_weight: float):
        new_form: list[(str, [(str, float)])] = []

        for node_i, node_inf in enumerate(self.nodes_form):
            if node_i == node_index:
                node_name, node_connections = node_inf

                new_connections = []
                for con_index, con in enumerate(node_connections):
                    if con_index == edge_index:
                        con_node, _ = con
                        new_connections.append((con_node, new_weight))
                    else:
                        new_connections.append(con)

                new_form.append((node_name, new_connections))
            else:
                new_form.append(node_inf)

    def update_edge_name(self, node_index: int, edge_index: int, edge_node_name: str):
        new_form: list[(str, [(str, float)])] = []

        for node_i, node_inf in enumerate(self.nodes_form):
            if node_i == node_index:
                node_name, node_connections = node_inf

                new_connections = []
                for con_index, con in enumerate(node_connections):
                    if con_index == edge_index:
                        _, con_weight = con
                        new_connections.append((edge_node_name, con_weight))
                    else:
                        new_connections.append(con)

                new_form.append((node_name, new_connections))
            else:
                new_form.append(node_inf)

        self.nodes_form = new_form

    def add_node_edge(self, node_index: int):
        new_form: list[(str, [(str, float)])] = []

        for node_i, node_inf in enumerate(self.nodes_form):
            if node_i == node_index:
                node_name, node_connections = node_inf
                new_form.append((node_name, node_connections + [('', '')]))
            else:
                new_form.append(node_inf)

        self.nodes_form = new_form

    def update_nodes_form(self):
        new_graph = Graph()

        # crear nodos
        for node in self.nodes_form:
            node_name, node_connections = node
            new_graph.add_node(node_name)

        # crear conecciones
        for node in self.nodes_form:
            node_name, node_connections = node


    def add_node(self):
        self.nodes_form.append(('', ''))

    def update_form(self, selected_graph):
        selected_graph_name, graph = selected_graph

        # actualizar el nombre del grafo
        self.graph_name = selected_graph_name

        # actualizar el formulario de nodos
        self.nodes_form = [(node.label, [(edge.node.label, edge.weight) for edge in node.edge_list]) for node in graph.node_list]

    def update_graph(self):
        pass
