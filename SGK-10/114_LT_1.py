n = int(input())

a = []

for i in range(n):
    x =input()
    a.append(x)

print(a)

del a[n - 1]

print(a)