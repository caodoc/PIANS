from math import sqrt

s = input()
s = s.split()

a = int(s[0])
b = int(s[1])
c = int(s[2])

p = (a + b + c ) / 2
s = sqrt(p * (p - a) * (p - b) * (p - c))

print('{0:0.1f}'.format(p * 2))
print('{0:0.1f}'.format(s))