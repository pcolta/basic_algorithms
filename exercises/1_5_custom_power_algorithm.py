# Algorytm potęgowania - A**B
from math import exp, log

a = 0
b = 0
while not a and not b:
    try:
        print("Wprowadź liczbę A:")
        a = int(input())
        print("Wprowadź liczbę B:")
        b = int(input())
    except ValueError:
        print("To nie liczba")

result_power = round(exp(b * log(a)))
print("Wynik potęgi {}**{} wynosi: {}".format(a, b, result_power))
