
def mochila(capacidad, pesos, valores):
    n = len(pesos)
    razones = [(valores[i] / pesos[i], pesos[i], valores[i]) for i in range(n)]
    razones.sort(reverse=True)
    total = 0
    seleccion = []
    for razon, peso, valor in razones:
        if capacidad >= peso:
            capacidad -= peso
            total += valor
            seleccion.append((peso, valor))
    return total, seleccion

capacidad = 5
pesos = [2, 3, 4]  # A, B, C (sin D)
valores = [12, 18, 20]

total, seleccion = mochila(capacidad, pesos, valores)
print("Valor total:", total)
print("Objetos seleccionados (peso, valor):", seleccion)
