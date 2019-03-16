# Analizowanie funkcji Ackermanna

def Ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return Ackermann(m - 1, n)
    elif m > 0 and m > 0:
        return Ackermann(m - 1, Ackermann(m, n - 1))

print(Ackermann(1,0))
