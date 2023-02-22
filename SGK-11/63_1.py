n = int(input())
a = []
cnt = 0

for i in range(n):
    x = int(input())
    a.append(x)

k = int(input())

for i in range(n):
    if a[i] % k == 0:
        cnt += 1

print(cnt)