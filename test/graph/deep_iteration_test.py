import sys
import unittest

from src.modules.graph.classes import GraphNode, Graph

# esto se hace para poder acceder a los módulos dentro de la carpeta src
sys.path.append('./')


class TestDFS(unittest.TestCase):
    def test_dfs(self):
        graph = Graph()
        node1 = GraphNode("1")
        node2 = GraphNode("2")
        node3 = GraphNode("3")
        node4 = GraphNode("4")
        node5 = GraphNode("5")
        node6 = GraphNode("6")
        node7 = GraphNode("7")
        node8 = GraphNode("8")
        node9 = GraphNode("9")
        node10 = GraphNode("10")
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
        real_value = graph.depth_first_search(graph.get_node(node1.label))
        expected_value = ['1', '2', '7', '9', '3', '8', '5', '4', '10', '6']
        self.assertEqual(real_value, expected_value)

    def test_bfs2(self):
        graph = Graph()
        node1 = GraphNode("A")
        node2 = GraphNode("B")
        node3 = GraphNode("C")
        node4 = GraphNode("D")
        node5 = GraphNode("E")
        node6 = GraphNode("F")
        node7 = GraphNode("G")
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
        real_value = graph.depth_first_search(graph.get_node(node4.label))
        expected_value = ['D', 'B', 'E', 'A', 'G', 'C', 'F']
        self.assertEqual(real_value, expected_value)


if __name__ == '__main__':
    unittest.main()
