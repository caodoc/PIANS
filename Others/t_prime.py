from math import sqrt

n = int(input())

def calc(x):
    temp = int(sqrt(x))
    if (temp ** 2 != x):
        return 0
    cnt = 0
    for i in range(1,int(sqrt(temp)) + 1):
        if (x % i == 0):
            if (x / i == i):
                cnt += 1
            else:
                cnt += 2
        if (cnt >= 3):
            return 0
    if (cnt == 2):
        return 1

res = 0

for i in range(2,n + 1):
    res += calc(i)

print(res)