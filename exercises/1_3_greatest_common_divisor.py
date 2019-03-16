# najwięszy wspólny dzielnik (NWD) liczb naturalnych A i B

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

less = min(a, b)
more = max(a, b)

for i in range(less):
    division = more % less
    if division == 0 or division == 1:
        print("NWD liczb {} i {} wynosi: {}".format(a, b, more / less))
        break
    else:
        less -= 1
