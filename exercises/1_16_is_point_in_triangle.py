from math import sqrt


def get_value():
    return [int(x) for x in input("Podaj wartości x y: ").split()]


print("Trójkąt ABC")
xa, ya = get_value()
xb, yb = get_value()
xc, yc = get_value()
print("Punkt")
xd, yd = get_value()

ab = sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
ac = sqrt((xc - xa) ** 2 + (yc - ya) ** 2)
bc = sqrt((xb - xc) ** 2 + (yb - yc) ** 2)
ad = sqrt((xa - xd) ** 2 + (ya - yd) ** 2)
bd = sqrt((xb - xd) ** 2 + (yb - yd) ** 2)
cd = sqrt((xc - xd) ** 2 + (yc - yd) ** 2)

if ad + cd > ac and ad + bd > ab and cd + bd > bc and ad + ab > ab and ad + bd < ac + cd:
    print("Punkt leży wewnątrz trójkąta")
else:
    print("Punkt leży na zewnątrz trójkąta")
