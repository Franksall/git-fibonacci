def fibonacci_iterativo(posicion, debe_imprimir):
    actual = 0
    siguiente = 1
    for x in range(posicion + 1):
        temporal = actual
        actual = siguiente
        siguiente = siguiente + temporal
    return temporal
posicion = 8
# Obtiene el valor pero no lo imprime con método iterativo
valor = fibonacci_iterativo(posicion, False)
print(f"\nFibonacci de {posicion} con método iterativo es {valor}")

#Se añade el  fibonacci recursivo para que asi se pueda eligirlo
def fibonacci_recursivo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)
    
posicion = 8
print(f"Fibonacci de {posicion} con método recursivo es ",fibonacci_recursivo(posicion))

#añadimos la ultima opcion de que seria un fibonacci de metodo memoria
nums = {}
def fibmemoria (n) :
    
    if n <= 2:
        return 1
    if n in nums:
        return nums [n]
    else:
        num = fibmemoria(n-1) + fibmemoria (n-2)
        nums [n]=num
        return num
#Mejoramos el codigo del fibonacci en memoria
print("Fibonaci de ",posicion," en metodo memoria es: ",fibmemoria(posicion))
