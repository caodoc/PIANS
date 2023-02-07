n = int(input())
a = []

for i in range(n):
    x = int(input())
    a.append(x)

b = a[::1]
b.sort()

print(b[0], a.index(b[0]))