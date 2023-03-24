def Tach_day(s):
    B = []
    C = []
    s = s.split()
    for i in range(len(s)):
        if (i % 2 != 0):
            C += s[i]
        else:
            B += s[i]
    return B, C

A = input()

print(Tach_day(A))