def power(a,b,c):
    return pow(a + b, c)

s = input()
r = s.split()
print(power(int(r[0]), int(r[1]), int(r[2])))