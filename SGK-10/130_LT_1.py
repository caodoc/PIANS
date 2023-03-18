def prime(x):
    for i in range(1,x + 1):
        if (n % i == 0):
            temp = 0
            for j in range(1,i + 1):
                if i % j == 0:
                    temp += 1
            if temp == 2:
                print(i, end = " ")

n = int(input())

prime(n)