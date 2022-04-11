def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
a=int(input("Fibonacci de: "))
print ("es: ",fib(a))
