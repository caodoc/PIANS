s = input()

res = 0

for i in s:
    if ('1' <= i <= '9'):
        res += int(i)

print(res)