n = int(input())
a = []

for i in range(n):
    x = int(input())
    a.append(x)

b = []

for i in range(n):
    s = 0
    for j in range(i + 1):
        s += a[j]
    b.append(s)

print(b)