def kruskal(grafo):
    grafo.sort()  # Ordenar por peso (menor a mayor)

    padre = {}
    def encontrar(nodo):
        if padre[nodo] != nodo:
            padre[nodo] = encontrar(padre[nodo])
        return padre[nodo]
    def unir(nodo1, nodo2):
        raiz1 = encontrar(nodo1)
        raiz2 = encontrar(nodo2)
        if raiz1 != raiz2:
            padre[raiz2] = raiz1
    nodos = set()
    for peso, u, v in grafo:
        nodos.add(u)
        nodos.add(v)
    for nodo in nodos:
        padre[nodo] = nodo
    mst = []
    total_peso = 0
    for peso, u, v in grafo:
        if encontrar(u) != encontrar(v):
            unir(u, v)
            mst.append((u, v, peso))
            total_peso += peso

    return mst, total_peso
grafo = [
    (4, 'A', 'B'),
    (2, 'A', 'C'),
    (5, 'B', 'C'),
    (10, 'B', 'D'),
    (3, 'C', 'D'),
    (7, 'C', 'E'),
    (8, 'D', 'E')
]
mst, costo_total = kruskal(grafo)

print("Aristas seleccionadas para conectar los edificios:")
for u, v, peso in mst:
    print(f"{u} - {v} (cable de {peso} m)")
print(f"Costo total (longitud de cable): {costo_total} m")
