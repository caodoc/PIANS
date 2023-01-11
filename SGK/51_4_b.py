import math

x = float(input())
y = float(input())
a = float(input())
b = float(input())
r = float(input())

d = math.sqrt((x - a) ** 2 + (y - b) ** 2)

if r >= d:
    print("YES")
    print(abs(x) + abs(y))
else:
    print("NO")
    print(x + y)