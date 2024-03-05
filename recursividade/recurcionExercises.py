#1 MDC

def mdc(a, b):
    if a == b:
        return a
    elif a < b:
        return mdc(b, a)
    return mdc(a-b, b)

print("1)", mdc(112, 42))

# 2

def produto(a, b):
    if b == 1:
        return a
    return a + produto(a, b-1)

print("2)", produto(5, 3))

# 3.1
listNumbers = [4, 1, 27, 27, 1, 10, 5, 2]

def getMaxNumber(numbers, current):
    if len(numbers) == 0:
        return current
    elif current < numbers[0]:
        return getMaxNumber(numbers[1:], numbers[0])
    return getMaxNumber(numbers[1:], current)

print("3.1)", getMaxNumber(listNumbers, listNumbers[0]))

# 3.2

def getMinNumber(numbers, current):
    if len(numbers) == 0:
        return current
    elif current > numbers[0]:
        return getMinNumber(numbers[1:], numbers[0])
    return getMinNumber(numbers[1:], current)

print("3.2)", getMinNumber(listNumbers, listNumbers[0]))

# 3.3

def getSum(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + getSum(numbers[1:])

print("3.3)", getSum(listNumbers))

def powerRecursion(b, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / powerRecursion(b, -n)
    return b * powerRecursion(b, n-1)

print("4)", powerRecursion(2, -2))

def soma(a, b):
    def succesor (x):
        return ( x + 1 )
    def antecesor (x):
        return ( x - 1 )
    if b == 0:
        return a
    if b > a:
        return soma(b, a)
    return soma(succesor(a), antecesor(b))

print("5)", soma(27, 3))

def numberOfZeros(n):
    if n == 0:
        return 1
    if n < 10:
        return 0
    if n % 10 == 0:
        return 1 + numberOfZeros(n // 10)
    return numberOfZeros(n // 10)

print("6)", numberOfZeros(2023030045))

def ex7(n):
    if n <= 0:
        return
    print(n)
    ex7(n-2)
    ex7(n-3)
    print(n)

print("7)")
ex7(4)    
    
    