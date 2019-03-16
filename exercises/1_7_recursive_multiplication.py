# rekurencyjne mnozenie liczb

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


def multiplication(a, b):
    if b == 1:
        return a
    elif b > 1:
        return a + a * (b - 1)


print(multiplication(a, b))
