s = input()

res = 0

for i in s:
    if (i == 'T'):
        res += 1
    else:
        res -= 1

print(abs(res))