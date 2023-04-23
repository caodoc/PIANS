from math import gcd

n = int(input())
m = int(input())

print(gcd(n, m))
print(n // gcd(n,m))
print(m // gcd(n, m))