def interativeFactorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print("interative", interativeFactorial(5))

def recursiveFactorial(n):
    if n == 0:
        return 1
    else:
        return n * recursiveFactorial(n-1)

print("recursive", interativeFactorial(5))

def Mdc(a, b):
    if b == 0:
        return a
    elif a < b:
        return Mdc(b, a)
    return Mdc(a-b, b)

print("MDC", Mdc(112, 42))