# algorytm okreslania liczb pierwszych

n = 0
while not n:
    try:
        print("Wprowadź liczbę N:")
        n = int(input())
    except ValueError:
        print("To nie liczba")

number_not_first = [i for i in range(2, n - 1) if n % i == 0]
if not number_not_first:
    print("Liczba {} jest liczba pierwsza".format(n))
else:
    print("Liczba {} nie jest liczba pierwsza".format(n))
