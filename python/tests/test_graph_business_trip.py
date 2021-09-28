import pytest
from code_challenges.graph.graph import Graph, Edge, Vertex
from code_challenges.graph_business_trip.graph_buiness_trip import business_trip

@pytest.mark.parametrize(
    'city_names, expected',
    [
        ([Metroville, Pandora, ]	True, $82
        [Arendelle, New Monstropolis, Naboo]	True, $115
        [Naboo, Pandora]	False, $0
        [Narnia, Arendelle, Naboo]


        # airports = [
#     "Metroville",
#     "Pandora",
#     "Arendelle",
#     "New_Monstropolis",
#     "Naboo",
#     "Narnia",
# ]

# routes = (["Metroville", "Pandora"],)
# ["Arendelle", "New_Monstropolis", "Naboo"]

def test_business_trip(city_names, expected):
    cities = Graph()
    metroville = cities.add_node("Metroville")
    pandora = cities.add_node("Pandora")
    arendelle = cities.add_node("Arendelle")
    new_monstropolis = cities.add_node("New Monstropolis")
    naboo = cities.add_node("Naboo")
    narnia = cities.add_node("Narnia")
    cities.add_edge(metroville, pandora, 82)
    cities.add_edge(pandora, metroville, 82)
    cities.add_edge(arendelle, new_monstropolis, 42)
    cities.add_edge(new_monstropolis, arendelle, 42)
    cities.add_edge(new_monstropolis, naboo, 73)
    cities.add_edge(naboo, new_monstropolis, 73)
    cities.add_edge(metroville, arendelle, 99)
    cities.add_edge(arendelle, metroville, 99)
    cities.add_edge(metroville, new_monstropolis, 105)
    cities.add_edge(new_monstropolis, metroville, 105)
    cities.add_edge(metroville, narnia, 37)
    cities.add_edge(narnia, metroville, 37)
    cities.add_edge(naboo, metroville, 26)
    cities.add_edge(metroville, naboo, 26)
    cities.add_edge(pandora, arendelle, 150)
    cities.add_edge(arendelle, pandora, 150)
    cities.add_edge(narnia, naboo, 250)
    cities.add_edge(naboo, narnia, 250)

    actual = business_trip(cities, city_names)
    assert actual == expected
