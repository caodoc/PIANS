import math

def ucln(a, b):
    return math.gcd(a, b)

s = input()
r = s.split()
print(ucln(int(r[0]), int(r[1])))