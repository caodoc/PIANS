from math import *

s = input()

s = s.split()

w = int(s[0])
h = float(s[1])

m = w / (h * h)

print('{0:0.1f}'.format(m))

if m < 20:
    print('Nguoi beo')
elif m >= 20 and m <= 30:
    print('Nguoi li tuong')
else:
    print('Nguoi map')