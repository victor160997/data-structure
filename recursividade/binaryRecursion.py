def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    print(f"call fib({n-1}) & fib({n-2})")
    return fibonacci(n-1) + fibonacci(n-2)

print (fibonacci(4))