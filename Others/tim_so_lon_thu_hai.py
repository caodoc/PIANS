n = int(input())
s = input()

s = s.split()
#s.sort()

#print(s)
a = b = -1e6 + 7

for i in range(n):
    if (int(s[i]) > a):
        b = a
        a = int(s[i])
    elif (int(s[i]) > b):
        b = int(s[i])

print(b)