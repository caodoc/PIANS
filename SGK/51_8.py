a = float(input())
b = float(input())

tmp = a + a * 0.003
res = 1

while a < b:
    a += a * 0.003
    res += 1

print(res)