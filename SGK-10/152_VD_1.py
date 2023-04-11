def calc(st, nd):
    cnt = 0
    for i in range(st,nd + 1):
        if (i % 4 == 0 and i % 100 != 0):
            cnt += 1

y1 = int(input())
y2 = int(input())

print(calc(y1,y2))
print(calc(2001,2101))