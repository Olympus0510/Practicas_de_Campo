#Función que calcula cómo dar cambio con la menor cantidad de monedas/billetes
def cambio_deMoneda(cantidad, denominaciones):
    denominaciones.sort(reverse=True)  
    resultado = {}
    for moneda in denominaciones:
        if cantidad >= moneda:
            num = cantidad // moneda
            cantidad -= num * moneda
            resultado[moneda] = num   
    return resultado

denominaciones = [500, 200, 100, 50, 20, 10, 5, 2, 1]
cantidad = 786
resultado = cambio_deMoneda(cantidad, denominaciones)
# Imprimir el desglose del cambio en billetes/monedas
print(f"Para entregar {cantidad} pesos, se debe dar:")
for denom, num in resultado.items():
    print(f"{num} billete(s)/moneda(s) de {denom} pesos")
