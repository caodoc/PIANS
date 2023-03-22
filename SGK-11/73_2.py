s = input()

s.lower()
r = ""
ar = []

for i in s:
    if ('a' <= i <= 'z'):
        if (r.find(i) == -1):
            r += i

for i in r:
    ar.append(s.count(i))

for i in range(len(r)):
    print(r[i], ar[i])