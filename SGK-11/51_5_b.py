i = 1
res = 1

while res > (2 * 10 ** -6):
    res += 1 / i
    i += 1

print(res)