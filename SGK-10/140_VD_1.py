def calc(a, b):
    while (a != b):
        if (a > b):
            a -= b
        else:
            b -= a
    bcnn = n * m / a
    return a, int(bcnn)

s = input()
s = s.split()
m = int(s[0])
n = int(s[1])

print(calc(n, m))