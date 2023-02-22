n = int(input())
a = []

for i in range(n):
    x = int(input())
    a.append(x)

ck = 1

while ck == 1:
    c = 1
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            tmp = a[i]
            a[i] = a[i + 1]
            a[i + 1] = tmp
            c = 0
    if c == 1:
        ck = 0

print(a)