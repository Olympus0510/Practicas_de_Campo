def factores_Primos(n):
    factores = []
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            factores.append(divisor)
            n //= divisor
        divisor += 1
    if n > 1:
        factores.append(n)
    return factores

# Numero a descomponer
numero = 84

# Ejecutamos la funcion
factores = factores_Primos(numero)
print(f"Los factores primos de {numero} son: {factores}")
