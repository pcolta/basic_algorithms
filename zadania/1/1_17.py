#Wieże Hanoi

src = [3,2,1]
dst = []
tmp = []

def is_hanoi(container):
    return container and len(container) == 3 and container == sorted(container)

while not is_hanoi(dst):
    if not dst or dst[-1] > src[-1]:
        blok = src.pop(-1)
        dst.append(blok)
    elif not tmp or tmp[-1] > src[-1]:
        blok = src.pop(-1)
        tmp.append(blok)
    elif not tmp or tmp[-1] > dst[-1]:
        blok = dst.pop(-1)
        tmp.append(blok)
    elif not src or src[-1 > dst[-1]]:
        blok = dst.pop(-1)
        src.append(blok)
    elif not src or src[-1] > tmp[-1]:
        blok = tmp.pop(-1)
        src.append(blok)
    elif not dst or dst[-1] > tmp[-1]:
        blok = tmp.pop(-1)
        dst.append(blok)

print(src)
print(dst)
print(tmp)