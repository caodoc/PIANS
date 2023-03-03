n = int(input())

a = []
a.append(0)

for i in range(1,n + 1):
    x = input()
    a.append(x)

print(a)

k = input()
a[0] = k

print(a)