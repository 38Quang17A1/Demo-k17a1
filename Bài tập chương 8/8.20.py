import math

def approximate_exp(x):
    approximation = 1.0
    term = x*x
    n = 2
    
    while term > 1e-4:
        approximation += term/n
        term *= x/n
        n += 1
    
    return approximation

x = 1
approximation = approximate_exp(x)
print("e ≈", approximation)