def sum(a, b):
    res = 0
    for i in range(a,b + 1):
        res += i
    return res

s = input()
r = s.split()
print(sum(int(r[0]), int(r[1])))