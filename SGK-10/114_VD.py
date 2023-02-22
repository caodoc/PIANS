n = int(input())

a = []

for i in range(n):
    x = float(input())
    a.append(x)

b = a[::1]
b.sort()

print(b[n - 1], a.index(b[n - 1]))