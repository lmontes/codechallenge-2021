# pip install numpy
import sys
import numpy as np


def dfs(G:np.array, node:int):
    visited = np.zeros(G.shape[0], dtype=np.int)

    def dfs_visit(G: np.array, node: int):
        for dest in np.nonzero(G[node])[0]:
            if not visited[dest]:
                visited[dest] = 1
                dfs_visit(G, dest)

    dfs_visit(G, node)

    # print("VISITED END: ", visited)

    return visited.sum()


def getCriticalCitiesThatCannotBeRemoved(tickets):
    city_names = set()
    for orig, dest in tickets:
        city_names.add(orig)
        city_names.add(dest)
    
    name2id = {}
    id2name = {}
    for id, city in enumerate(sorted(city_names)):
        name2id[city] = id
        id2name[id] = city 

    number_of_cities = len(city_names)

    # Creamos el grafo, matriz de numpy
    graph = np.zeros((number_of_cities, number_of_cities), dtype=np.int)
    for orig, dest in tickets:
        graph[name2id[orig]][name2id[dest]] = 1
        graph[name2id[dest]][name2id[orig]] = 1

    # Iteramos por todos los nodos desconectandolos para ver si son criticos
    critical_nodes = []
    for node in range(number_of_cities):
        # Grafo auxiliar donde desconectamos un nodo
        graph_aux = graph.copy()
        graph_aux[node,:] = 0
        graph_aux[:,node] = 0

        # DFS sobre un nodo diferente al que estamos intentando eliminar
        total_visited = dfs(graph_aux, (node + 1) % number_of_cities)

        # Si el nodo eliminado es critico visitaremos menos nodos
        # que el total de ciudades menos 1
        if total_visited < number_of_cities - 1:
            critical_nodes.append(node)

    if len(critical_nodes) == 0:
        cities = ["-"]
    else:
        cities = [id2name[node] for node in critical_nodes]

    return list(sorted(cities))


N = int(sys.stdin.readline())

for i in range(0, N):
    T = int(sys.stdin.readline())

    tickets = []
    for _ in range(0, T):
        ticket = sys.stdin.readline().strip()
        orig, dest = list(map(str.strip, ticket.split(",")))
        tickets.append((orig, dest))
    # print(tickets)
    
    cities = getCriticalCitiesThatCannotBeRemoved(tickets)
    result = ",".join(cities)

    print(f"Case #{i+1}: {result}")
