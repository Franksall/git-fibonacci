#Creamos el menu iterativo para que si nos podamos el fibonacci que 
#quedramos hallar
menu = """
Menu
1.-Fibonacci manera iterativa
2.-Fibonacci manera recursiva
3.-Fibonacci manera Memoria
"""
print(menu)
op=int(input("Elige alguna opcion: "))
if op == 1:
    def fibonacci_iterativo(posicion, debe_imprimir):
        actual = 0
        siguiente = 1
        for x in range(posicion + 1):#un for para que haci en el rango de la posiccion dada imprima su fibonacci
            if debe_imprimir:
                print("[",x,"] = ",str(actual,) + "\n", end="")
            temporal = actual
            actual = siguiente
            siguiente = siguiente + temporal
        return temporal
    posicion = int(input("Fibonacci de: "))
    # Imprime los fibonacci de los numeros hasta la posicion dada
    print(f"Imprimiendo serie de numeros hasta la  posición {posicion}")
    fibonacci_iterativo(posicion, True)
    # Obtiene el valor pero no lo imprime con método iterativo
    valor = fibonacci_iterativo(posicion, False)
    print(f"\nFibonacci de {posicion} con método iterativo es {valor}")
elif op == 2:
    #Se añade el  fibonacci recursivo para que asi se pueda eligirlo
    def fibonacci_recursivo(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)
    
    posicion = int(input("Fibonacci de: "))
    for n1 in range(1,posicion):
        print("[",n1,"] = ",fibonacci_recursivo(n1))
    # Obtiene el valor pero no lo imprime con método recursivo
    print(f"Fibonacci de {posicion} con método recursivo es ",fibonacci_recursivo(posicion))
elif op == 3:
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
    posicion = int(input("Fibonacci de: "))
    for n1 in range(1,posicion):
        print("[",n1,"] = ",fibmemoria(n1))
    print("Fibonaci de ",posicion," en metodo memoria es: ",fibmemoria(posicion))
else:
    print("Tecla error")



