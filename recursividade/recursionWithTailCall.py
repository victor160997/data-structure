def tailFactorial(n, accumulator=1):
    if n == 0:
        return accumulator
    elif n == 1:
        return accumulator
    else:
        return tailFactorial(n-1, n*accumulator)

print("tailFactorial", tailFactorial(5))

def tailFibonacci(n, currrent=0, next=1):
    if n == 0:
        return currrent
    if n == 1:
        return next
    print(f"call fib({n-1}, {next}, {currrent+next})")
    return tailFibonacci(n-1, next, currrent+next)

print("tailFibonacci", tailFibonacci(8))
    
# avoid stack overflow