s = input()

s = s.split()
a = int(s[0])
b = int(s[1])
c = int(s[2])

if c - b >= b - a:
    print(c - b - 1)
else:
    print(b - a - 1)