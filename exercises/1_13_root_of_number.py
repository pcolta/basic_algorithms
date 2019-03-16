# obliczanie pierwiastkow
from math import sqrt

a = 0
b = 0
c = 0
while not a and not b:
    try:
        print("Wprowadź liczbę A:")
        a = int(input())
        print("Wprowadź liczbę B:")
        b = int(input())
        print("Wprowadź liczbę C:")
        c = int(input())
    except ValueError:
        print("To nie liczba")

print("f(x) = {}x**2 + {}x + {}".format(a, b, c))

delta = b ** 2 - 4 * a * c
if delta > 0:
    x1 = (-b - sqrt(delta)) / 2 * a
    x2 = (-b + sqrt(delta)) / 2 * a
    print("Istnieją dwa pierwiastki i wynoszą: {}, {}".format(x1, x2))
elif delta == 0:
    x0 = -b / 2 * a
    print("Istnieje jeden pierwiastek i wynosi: {}".format(x0))
else:
    "Brak pierwiastków"
