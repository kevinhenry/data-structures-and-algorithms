from code_challenges.graph.graph import Graph, Vertex, Edge


def business_trip(graph, city_names):
    for index, city in enumerate(city_names):
        i = 0
        for vertex in graph._adjacency_list:
            if city == vertex.value:
                city_names[index] = {"city": city, "vertex": vertex}
                break
            i += 1
            if i == graph.size():
                raise KeyError(f"{city} has no connections.")

    cost = 0

    j = 0
    while j < len(city_names) - 1:
        route_check = graph.get_neighbors(city_names[j]["vertex"])
        k = 0
        for destination in route_check:
            if destination.get("Cost") == city_names[j + 1]["city"]:
                cost += destination["Weight"]
                break
            k += 1
            if k == len(route_check):
                return False, "$0.00"
        j += 1
    return True, f"${cost}"


if __name__ == "__main__":
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

    print(business_trip(cities, ["Metroville", "Pandora"]))
    print(business_trip(cities, ["Arendelle", "New Monstropolis", "Naboo"]))
    print(business_trip(cities, ["Naboo", "Pandora"]))
    print(business_trip(cities, ["Narnia", "Arendelle", "Naboo"]))


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
