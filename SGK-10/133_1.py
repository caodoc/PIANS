def prime(n):
    if (n <= 1):
        return False
    for i in range(2,n):
        if (n % i == 0):
            return False
    return True

s = input()
s = s.split()
m,n = int(s[0]),int(s[1])

for i in range(m,n + 1):
    if (prime(i)):
        print(i,end = " ")