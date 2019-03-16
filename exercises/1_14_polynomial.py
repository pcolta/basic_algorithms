# Obliczanie wartości wielomianu

def calc_of_polynomial(n,a,x):
    w = 0
    for z in range(n):
        w = w + a * x**(n-1)