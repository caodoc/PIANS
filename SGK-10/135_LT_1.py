def power(a,b,c):
    res = 1
    for i in range(c):
        res *= (a + b)
    return res

s = input()
r = s.split()
print(power(int(r[0]), int(r[1]), int(r[2])))