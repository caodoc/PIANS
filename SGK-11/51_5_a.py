n = 1
res = 0

while n <= 50:
    res += n / (n + 1)
    n += 1
print('{0:0.1f}'.format(res))