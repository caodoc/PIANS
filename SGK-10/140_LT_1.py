def calc(s):
    s = s.split()
    cList = []
    for i in s:
        cList += i[0]
    return cList

sList = input()

print(calc(sList))