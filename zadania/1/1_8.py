# obliczanie ciagu Fibonacciego

n = 0
while not n:
    try:
        print("Wprowadź liczbę N:")
        n = int(input())
    except ValueError:
        print("To nie liczba")


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(n))
