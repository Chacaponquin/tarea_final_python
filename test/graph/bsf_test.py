import sys
import unittest

# esto se hace para poder acceder a los módulos dentro de la carpeta src
sys.path.append('./')

from src.modules.graph.classes.Graph import Graph
from src.modules.graph.classes.GraphNode import GraphNode


class Testbsf(unittest.TestCase):
    def test_bfs(self):
        graph = Graph()
        node1 = GraphNode("jose")
        node2 = GraphNode("amaya")
        node3 = GraphNode("hector")
        node4 = GraphNode("brian")
        node5 = GraphNode("amanda")
        node6 = GraphNode("nanda")
        node7 = GraphNode("camilo")
        node8 = GraphNode("david")
        node9 = GraphNode("ale")
        node10 = GraphNode("gabriela")
        graph.add_node(node1.label)
        graph.add_node(node2.label)
        graph.add_node(node3.label)
        graph.add_node(node4.label)
        graph.add_node(node5.label)
        graph.add_node(node6.label)
        graph.add_node(node7.label)
        graph.add_node(node8.label)
        graph.add_node(node9.label)
        graph.add_node(node10.label)
        graph.connect(node1.label, node2.label, 5)
        graph.connect(node1.label, node3.label, 5)
        graph.connect(node1.label, node4.label, 5)
        graph.connect(node2.label, node7.label, 5)
        graph.connect(node2.label, node9.label, 5)
        graph.connect(node3.label, node8.label, 5)
        graph.connect(node4.label, node7.label, 5)
        graph.connect(node4.label, node9.label, 5)
        graph.connect(node4.label, node10.label, 5)
        graph.connect(node4.label, node5.label, 5)
        graph.connect(node8.label, node5.label, 5)
        graph.connect(node10.label, node6.label, 5)
        real_value = graph.bfs(graph.get_node(node1.label))
        expected_value = ['jose', 'amaya', 'hector', 'brian', 'camilo', 'ale', 'david', 'gabriela', 'amanda', 'nanda']
        self.assertEqual(real_value, expected_value)

    def test_bfs2(self):
        graph = Graph()
        node1 = GraphNode("A")
        node2 = GraphNode("B")
        node3 = GraphNode("C")
        node4 = GraphNode("D")
        node5 = GraphNode("H")
        node6 = GraphNode("R")
        node7 = GraphNode("T")
        graph.add_node(node1.label)
        graph.add_node(node2.label)
        graph.add_node(node3.label)
        graph.add_node(node4.label)
        graph.add_node(node5.label)
        graph.add_node(node6.label)
        graph.add_node(node7.label)
        graph.connect(node4.label, node2.label, 5)
        graph.connect(node4.label, node3.label, 5)
        graph.connect(node2.label, node5.label, 5)
        graph.connect(node3.label, node6.label, 5)
        graph.connect(node5.label, node1.label, 5)
        graph.connect(node5.label, node7.label, 5)
        graph.connect(node5.label, node4.label, 5)
        graph.connect(node6.label, node5.label, 5)
        real_value = graph.bfs(graph.get_node(node4.label))
        expected_value = ['D', 'B', 'C', 'H', 'R', 'A', 'T']
        self.assertEqual(real_value, expected_value)


if __name__ == '__main__':
    unittest.main()
