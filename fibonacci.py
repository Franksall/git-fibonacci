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
def fibonaccir(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    else:
      v=fibonaccir(n-1) + fibonaccir(n-2)
    return v

xr = list(range(1,11))           # 1..10 lista de valores
fr = []             # A su vez es el cuadrado de n, el cubo de n, el valor de n Fibonacci
for v in xr:                     #Secuencialmente valores de la función de la computadora
    fr.append(fibonaccir(v))

print("fib Recursivo(n)=",fr)
nums = {}
def fibonaccimemo(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    if n in nums:
        return nums [n]
    else:
        num = fibonaccimemo(n-1) + fibonaccimemo (n-2)
        nums [n]=num
        return num

xnemo = list(range(1,11))           # 1..10 lista de valores
fmemo = []             # A su vez es el cuadrado de n, el cubo de n, el valor de n Fibonacci
for v in xnemo:                     #Secuencialmente valores de la función de la computadora
    fmemo.append(fibonaccimemo(v))

print("fib Memoria(n)=",fmemo)
def fibonaccilog(n):
    even = lambda n: (n % 2 == 0)

    (current, next, p, q) = (0, 1, 0, 1)    

    while (n > 0):
        if (even(n)):
            (p, q) = (p**2 + q**2, q**2 + 2*p*q)
            n /= 2
        else:
            (current, next) = (p*current + q*next, q*current + (p+q)*next)
            n -= 1
    
    return current
xlog = list(range(1,11))           # 1..10 lista de valores
filog = []             # A su vez es el cuadrado de n, el cubo de n, el valor de n Fibonacci
for v in xlog:                     #Secuencialmente valores de la función de la computadora
    filog.append(fibonaccilog(v))

print("fib Logaritmico(n)=",filog)