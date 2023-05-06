from src.modules.graph.classes.GraphNode import GraphNode


class Graph:
    def __init__(self):
        self.node_list = []

    def add_node(self, label):
        node = self.get_node(label)
        if node is None:
            self.node_list.append(GraphNode(label))
        return node is None

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

    def connect(self, label_1, label_2, weight):
        node_1 = self.get_node(label_1)
        node_2 = self.get_node(label_2)
        return node_1.add_edge(node_2, weight)

    def connect_nodes(self, node_1, node_2, weight):
        return self.connect(node_1.label, node_2.label, weight)

    def disconnect(self, label_1, label_2):
        node_1 = self.get_node(label_1)
        node_2 = self.get_node(label_2)
        return node_1.delete_edge(node_2)

    def disconnect_nodes(self, node_1, node_2):
        return self.disconnect(node_1.label, node_2.label)

    def are_adjacent(self, node_1, node_2):
        return node_1.is_adjacent(node_2)

    def get_depth_first_search(self, node):
        visited = []
        if len(node.edge_list) > 0:
            self.depth_first_search(node, visited)
        return visited

    def depth_first_search(self, node, visited):
        if node.label not in visited:
            visited.append(node.label)
        for edge in node.edge_list:
            if edge.node.label not in visited:
                self.depth_first_search(edge.node, visited)

graph = Graph()
node1 = GraphNode("jose")
node2 = GraphNode("amaya")
node3 = GraphNode("hector")
graph.add_node(node1.label)
graph.add_node(node2.label)
graph.add_node(node3.label)
print(graph.connect(node1.label, node2.label, 5))
print(len(graph.node_list[0].edge_list))
graph.disconnect(node1.label, node2.label)
print(len(graph.node_list[0].edge_list))
graph.connect(node1.label, node2.label, 5)
graph.connect(node1.label, node3.label, 5)
print(graph.get_depth_first_search(graph.node_list[0]))

