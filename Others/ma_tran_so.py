n = int(input())

ar = []

for i in range(n):
    s = input()
    s = s.split()
    t = []
    for j in range(n):
        t.append(int(s[j]))
    ar.append(t)

r1 = r2 = 0

#print(ar)

for i in range(n):
    r1 += ar[i][i]
for i in range(n - 1,-1,-1):
    r2 += ar[i][i]

print(r1)
print(r2)