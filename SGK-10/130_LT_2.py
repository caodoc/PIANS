def numbers(x):
    cnt = 0
    for i in x:
        if i >= '0' and i <= '9':
            cnt += 1
    return cnt

s = input()

print(numbers(s))