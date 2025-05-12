import math
import heapq

def ruta_mas_corta(grafo, inicio, destino):
    dist = {nodo: math.inf for nodo in grafo}
    dist[inicio] = 0
    pq = [(0, inicio)]
    while pq:
        actual_dist, actual = heapq.heappop(pq)
        if actual == destino:
            return actual_dist
        for vecino, peso in grafo[actual]:
            nuevo_dist = actual_dist + peso
            if nuevo_dist < dist[vecino]:
                dist[vecino] = nuevo_dist
                heapq.heappush(pq, (nuevo_dist, vecino))
    return math.inf
# Definimos el grafo de las ciudades
grafo = {
    'Ciudad1': [('Ciudad2', 4), ('Ciudad3', 2)],
    'Ciudad2': [('Ciudad1', 4), ('Ciudad3', 5), ('Ciudad4', 10)],
    'Ciudad3': [('Ciudad1', 2), ('Ciudad2', 5), ('Ciudad4', 3)],
    'Ciudad4': [('Ciudad2', 10), ('Ciudad3', 3)]
}
# Queremos ir de Ciudad1 a Ciudad4
inicio = 'Ciudad1'
destino = 'Ciudad4'
# Ejecutamos la funcion
distancia = ruta_mas_corta(grafo, inicio, destino)
print(f"La distancia mas corta de {inicio} a {destino} es {distancia} km")
