def fibonacci(n):
    if n <= 2:
        return 1
    a,b = 1,1           # El valor de los dos últimos elementos, a es el elemento anterior, b es el elemento anterior
    for x in range(3,n+1):
        v = a + b       #     = la suma de los dos primeros
        a,b = b,v       #a = b, b = v
    return v

xite = list(range(1,11))           # 1..10 lista de valores
fn = []             # A su vez es el cuadrado de n, el cubo de n, el valor de n Fibonacci
for v in xite:                     #Secuencialmente valores de la función de la computadora
    fn.append(fibonacci(v))

print("fib Iterativo (n)=",fn)