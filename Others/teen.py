s = input()

t = 0
e = 0
n = 0
res = 0

for i in s:
    if (i == 'T'):
        t += 1
    if (i == 'E'):
        e += 1
    if (i == 'N'):
        n += 1

while (t > 0 and e > 0 and n > 0):
    res += 1
    t -= 1
    e -= 2
    n -= 1

print(res)