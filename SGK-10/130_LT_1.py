def prime(x):
    cnt = 0
    for i in range(1,x + 1):
        if (n % i == 0):
            cnt += 1
    return cnt

n = int(input())

print(prime(n))