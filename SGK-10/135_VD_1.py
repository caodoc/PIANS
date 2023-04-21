def ucln(a, b):
    while (a != b):
        if (a > b):
            a -= b
        else:
            b -= a
    return a

s = input()
r = s.split()
print(ucln(int(r[0]), int(r[1])))