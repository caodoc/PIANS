from math import sqrt

s = input()

s = s.split()

a = int(s[0])
b = int(s[1])
res = 0

def calc(x):
    cnt = 1
    for i in range(2, x):
        if (x % i == 0):
            cnt += i
    return cnt
for i in range(a, b + 1):
    if (calc(i) > i):
        res += 1
        #print(i)

print(res)