a = int(input())
b = int(input())

t1 = max(a, b)
t2 = min(a, b)

i = 0

while t2 * 2 < t1:
    t1 += 1
    t2 += 1
    i += 1

print(i)