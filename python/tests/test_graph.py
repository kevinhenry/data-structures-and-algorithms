import pytest
from code_challenges.graph.graph import Vertex, Graph


def test_add_vertex_pass():
    vertex = Vertex("a")
    actual = vertex.value
    expected = "a"
    assert actual == expected


def test_add_vertex_fail():
    vertex = Vertex("a")
    actual = vertex.value
    expected = "b"
    assert actual != expected


# Node can be successfully added to the graph
def test_add_node():
    graph = Graph()
    expected = "a"
    actual = graph.add_node("a").value
    assert expected == actual


# An edge can be successfully added to the graph
def test_add_edge_true():
    graph = Graph()
    a = graph.add_node("a")
    b = graph.add_node("b")
    graph.add_edge(a, b)
    assert True


# A collection of all nodes can be properly retrieved from the graph
def test_get_nodes():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    actual = graph.get_nodes()
    expected = ["a", "b"]
    assert actual == expected


# An empty graph properly returns null
def test_get_nodes_empty():
    graph = Graph()
    actual = graph.get_nodes()
    expected = None
    assert actual == expected


# A graph with only one node and edge can be properly returned
def test_one_node_one_edge_start():
    graph = Graph()
    a = graph.add_node("a")
    b = "b"
    with pytest.raises(KeyError) as e:
        graph.add_edge(b, a)


def test_one_node_one_edge_end():
    graph = Graph()
    a = graph.add_node("a")
    b = "b"
    with pytest.raises(KeyError):
        graph.add_edge(a, b)


# All appropriate neighbors can be retrieved from the graph
# Neighbors are returned with the weight between nodes included
def test_get_neighbors():
    graph = Graph()
    a = graph.add_node("a")
    b = graph.add_node("b")
    graph.add_edge(a, b)
    actual = graph.get_neighbors("a")
    expected = ["b", 1]
    assert actual == expected


# The proper size is returned, representing the number of nodes in the graph
def test_add_size():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    expected = 2
    actual = graph.size()
    assert actual == expected


def test_add_size_fail():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    expected = 3
    actual = graph.size()
    assert actual != expected
