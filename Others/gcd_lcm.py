from math import gcd

a = int(input())
b = int(input())

print(gcd(a, b))
print(a * b / gcd(a, b))