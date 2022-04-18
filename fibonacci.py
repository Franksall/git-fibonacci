def fibonacci_iterativo(posicion, debe_imprimir):
    actual = 0
    siguiente = 1
    for x in range(posicion + 1):
        if debe_imprimir:
            print(str(actual) + ",", end="")
        temporal = actual
        actual = siguiente
        siguiente = siguiente + temporal
    return temporal

def fibonacci_recursivo(posicion):
    if posicion < 2:
        return posicion
    return fibonacci_recursivo(posicion - 1) + fibonacci_recursivo(posicion - 2)
posicion = int(input("Fibonacci de: "))

print(f"Imprimiendo serie de numeros hasta la  posición {posicion}")
fibonacci_iterativo(posicion, True)

valor = fibonacci_iterativo(posicion, False)
print(f"\nFibonacci de {posicion} con método iterativo es {valor}")

valor = fibonacci_recursivo(posicion)
print(f"Fibonacci de {posicion} con método recursivo es {valor}")
