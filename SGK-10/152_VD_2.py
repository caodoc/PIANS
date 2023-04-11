def ucln(x, y):
    if (y == 0):
        return x
    return ucln(y, x % y)
    
s = input()
s = s.split()
a = int(s[0])
b = int(s[1])

print(ucln(a, b))