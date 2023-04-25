n = int(input())
s = input()

s = s.split()

sum = 0

for i in range(n):
    s[i] = int(s[i])
    sum += s[i]

if (sum % n != 0):
    print(-1)
else:
    res = 0
    tb = sum / n
    for i in range(n):
        if tb > s[i]:
            res += tb - s[i]
    print(int(res))