n = int(input())

a = []

for i in range(n):
    x = float(input())
    a.append(x)

if (n % 2 == 0):
    a.remove(a[int(n / 2)])
    a.remove(a[int(n / 2 - 1)])
else:
    a.remove(a[int(n / 2)])

print(a)