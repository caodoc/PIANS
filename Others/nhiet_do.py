a = []
s = 0
cnt = 0

for i in range(7):
    x = float(input())
    a.append(x)
    s += i

s /= 7

for i in range(7):
    if a[i] > s: cnt += 1

print('{0:0.4f}'.format(s))
print(cnt)