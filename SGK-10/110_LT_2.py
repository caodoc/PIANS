res = 0

for i in range(1,101):
    if (i % 5 == 0 or i % 3 == 1):
        res += 1
        #print(i)

print(res)