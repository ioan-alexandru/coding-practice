def leastFactorial(n):
    i = 2
    product = 1
    while product < n:
        product *= i
        i += 1
    return product
