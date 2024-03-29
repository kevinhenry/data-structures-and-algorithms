import pytest
from code_challenges.graph.graph import Graph, Edge, Vertex


@pytest.fixture(scope="function")
def test_graph():
    graph = Graph()
    a = graph.add_node("a")
    b = graph.add_node("b")
    c = graph.add_node("c")
    d = graph.add_node("d")
    e = graph.add_node("e")
    f = graph.add_node("f")
    g = graph.add_node("g")
    h = graph.add_node("h")
    graph.add_edge(a, b)
    graph.add_edge(a, c)
    graph.add_edge(b, d)
    graph.add_edge(c, d)
    graph.add_edge(a, e)
    graph.add_edge(e, f)
    graph.add_edge(e, g)
    graph.add_edge(f, h)
    return graph


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
def test_get_neighbor():
    graph = Graph()
    a = graph.add_node("a")
    b = graph.add_node("b")
    graph.add_edge(a, b)
    actual = graph.get_neighbor("a")
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


def test_breadth_first(test_graph):
    assert test_graph.breadth_first("a") == ["a", "b", "c", "e", "d", "f", "g", "h"]


def test_breadth_first_fail(test_graph):
    try:
        test_graph.breadth_first("i")
        assert False
    except KeyError:
        assert True


def test_depth_first(test_graph):
    assert test_graph.depth_first("a") == ["a", "b", "d", "c", "e", "f", "h", "g"]


def test_depth_first_fail(test_graph):
    try:
        test_graph.depth_first("k")
        assert False
    except KeyError:
        assert True
