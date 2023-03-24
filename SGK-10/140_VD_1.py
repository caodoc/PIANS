import math

def calc(a, b):
    ucln = math.gcd(a, b)
    bcnn = n * m / ucln
    return ucln, bcnn

s = input()
s = s.split()
m = int(s[0])
n = int(s[1])

print(calc(n, m))