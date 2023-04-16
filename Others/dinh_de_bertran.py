n = int(input())

res = 0

def calc(x):
    for i in range(2, x):
        if (i * i > x):
            break
        if (x % i == 0):
            return False
    return True

for i in range(n + 1, n * 2):
    if (calc(i)):
        res += 1

print(res)