# Algorytm znajdowania najmniejszej wspólnej wielokrotności(NWW)

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
        nww = a * b / (more / less)
        print("NWW liczb {} i {} wynosi: {}".format(a, b, nww))
        break
    else:
        less -= 1
