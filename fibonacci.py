def fibonacci_iterativo(posicion, debe_imprimir):
    actual = 0
    siguiente = 1
    for x in range(posicion + 1): #un for para que haci en el rango de la posiccion dada imprima su fibonacci
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
# Imprime los fibonacci de los numeros hasta la posicion dada
print(f"Imprimiendo serie de numeros hasta la  posición {posicion}")
fibonacci_iterativo(posicion, True)
# Obtiene el valor pero no lo imprime con método iterativo
valor = fibonacci_iterativo(posicion, False)
print(f"\nFibonacci de {posicion} con metodo iterativo es {valor}")
# Obtiene el valor pero no lo imprime con método recursivo
valor = fibonacci_recursivo(posicion)
print(f"Fibonacci de {posicion} con metodo recursivo es {valor}")
