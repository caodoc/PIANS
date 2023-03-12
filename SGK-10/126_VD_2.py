n = int(input())

s = []
res = 0

for i in range(n):
    s.append(input())

k = input()

for i in range(n):
    if (s[i].find(k) != -1):
        res += 1

print(res)