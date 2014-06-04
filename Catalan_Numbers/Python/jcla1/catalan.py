def catalan_direct(n):
    return factorial(2 * n) / (factorial(n + 1) * factorial(n))

def catalan_binomial(n):
    if n == 0: return 1
    return binomial_coefficient(2 * n, n) - binomial_coefficient(2 * n, n - 1)

def binomial_coefficient(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

def factorial(n):
    return n * factorial(n-1) if n > 1 else 1