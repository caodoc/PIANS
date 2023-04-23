from math import gcd

n = int(input())

cnt = 0

for i in range(1,n):
    if (gcd(i, n) == 1):
        cnt += 1

print(cnt)