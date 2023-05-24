from src.modules.graph.classes import GraphNode, Graph


class GraphForm:
    def __init__(self, selected_graph: (str, Graph)):
        self.selected_graph: (str, Graph) = selected_graph

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

        self.nodes_form = new_form

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

    def delete_edge(self, node_index: int, edge_index: int):
        new_form: list[(str, [(str, float)])] = []

        for node_i, node_inf in enumerate(self.nodes_form):
            if node_i == node_index:
                node_name, node_connections = node_inf

                new_connections = []
                for con_index, con in enumerate(node_connections):
                    if con_index != edge_index:
                        new_connections.append(con)

                new_form.append((node_name, new_connections))
            else:
                new_form.append(node_inf)

        self.nodes_form = new_form

    def delete_node(self, node_index: int):
        new_form: list[(str, list[(str, float)])] = []

        # borrar el nodo del formulario
        node_deleted = None
        for node_i, node_inf in enumerate(self.nodes_form):
            if node_index != node_i:
                new_form.append(node_inf)
            else:
                node_name, _ = node_inf
                # si se encuentra se borra y se guarda el nombre
                node_deleted = node_name

        # borrar en el resto de nodos cualquier conexion con el nodo eliminado
        save_form: list[(str, list[(str, float)])] = []
        for node_inf in new_form:
            node_name, node_connections = node_inf

            new_connections: list[(str, float)] = []
            for con in node_connections:
                con_node, con_weight = con

                if con_node != node_deleted:
                    new_connections.append(con)

            save_form.append((node_name, new_connections))

        self.nodes_form = save_form

    def add_node_edge(self, node_index: int):
        new_form: list[(str, [(str, float)])] = []

        for node_i, node_inf in enumerate(self.nodes_form):
            if node_i == node_index:
                node_name, node_connections = node_inf

                # conexiones posibles
                posible_connections = self.get_node_posible_connections()
                new_form.append((node_name, node_connections + [(posible_connections[0], 0)]))
            else:
                new_form.append(node_inf)

        self.nodes_form = new_form

    def get_node_posible_connections(self) -> list[str]:
        return_nodes: list[str] = []

        for node in self.nodes_form:
            node_name, _ = node
            return_nodes.append(node_name)

        return return_nodes

    def update_nodes_form(self):
        new_graph = Graph()

        # crear nodos
        for node in self.nodes_form:
            node_name, node_connections = node
            new_graph.add_node(node_name)

        # crear conexiones
        for node in self.nodes_form:
            node_name, node_connections = node

            for con in node_connections:
                con_node, con_weight = con
                new_graph.connect(node_name, con_node, con_weight)

        return new_graph

    def add_node(self):
        self.nodes_form.append(('', []))

    def update_form(self, selected_graph):
        selected_graph_name, graph = selected_graph

        # actualizar el nombre del grafo
        self.graph_name = selected_graph_name

        # actualizar el formulario de nodos
        self.nodes_form = [(node.label, [(edge.node.label, edge.weight) for edge in node.edge_list]) for node in graph.node_list]

    def update_graph(self):
        pass
