from src.modules.graph.classes import GraphNode, Graph

class GraphForm:
    def __init__(self, selected_graph: Graph):
        self.selected_graph = selected_graph

        self.graph_name: str = ''
        self.nodes_form: list[(str, str)] = []

        self.update_form(self.selected_graph)

    def update_node_name(self, node_index: int, new_node_name: str):
        new_form: list[(str, str)] = []

        for node_i, node_inf in enumerate(self.nodes_form):
            if node_index == node_i:
                _, connection = node_inf
                new_form.append((new_node_name, connection))
            else:
                new_form.append(node_inf)

        self.nodes_form = new_form
        print(self.nodes_form)

    def update_node_connections(self, node_index: int, new_connections: str):
        new_form: list[(str, str)] = []

        for node_i, node_inf in enumerate(self.nodes_form):
            if node_index == node_i:
                node_name, _ = node_inf
                new_form.append((node_name, new_connections))
            else:
                new_form.append(node_inf)

        self.nodes_form = new_form
        print(self.nodes_form)

    def update_nodes_form(self):
        pass

    def add_node(self):
        self.nodes_form.append(('', ''))

    def update_form(self, selected_graph):
        selected_graph_name, graph = selected_graph

        # actualizar el nombre del grafo
        self.graph_name = selected_graph_name

        # actualizar el formulario de nodos
        self.nodes_form = [(node.label, self.get_node_connections_string(node)) for node in graph.node_list]

    def get_node_connections_string(self, node: GraphNode) -> str:
        labels_list: list[str] = list(map(lambda n: n.label, node.get_adjacents_nodes()))

        return ', '.join(labels_list)

    def update_graph(self):
        pass
