n = int(input())

ar = []
res = 0
s = "Huong"

for i in range(n):
    x = input()
    ar.append(x)

for i in range(n):
    if s in ar[i]:
        res += 1

print(res)