from math import sqrt

n = int(input())

a = []
chan = 0
le = 0
ngto = 0

for i in range(n):
    a.append(int(input()))

for i in a:
    if (i % 2 == 0):
        chan += 1
    else:
        le += 1
    cnt = 0
    for j in range(1,int(sqrt(i))): 
        if (i % j == 0): 
            if (i / j == j):
                cnt += 1
            else:
                cnt += 2
    if (cnt == 2):
        ngto += 1

print(le, chan, ngto)