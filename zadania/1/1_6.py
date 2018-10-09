# znajdz silnie danej liczny (N!)

n = 0
while not n:
    try:
        print("Wprowadź liczbę N:")
        n = int(input())
    except ValueError:
        print("To nie liczba")

a = n


def silnia(n):
    if n == 0:
        return 1
    elif n > 0:
        return n * silnia(n - 1)


print("Silnia z liczby {} wynosi: {}".format(a, silnia(n)))
