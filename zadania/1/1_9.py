# algorytm podnoszenia 2 do potęgi naturalnej

n = 0
while not n:
    try:
        print("Wprowadź liczbę N:")
        n = int(input())
    except ValueError:
        print("To nie liczba")


def power_2_N(n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return (2 ** (n / 2)) ** 2
    elif n % 2 == 1:
        return 2 * (2 ** (n / 2)) ** 2


print("2 podniesione do potęgi {} wynosi: {}".format(n, power_2_N(n)))
