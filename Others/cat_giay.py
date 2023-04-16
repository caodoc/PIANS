s = input()
s = s.split()

a = int(s[0])
b = int(s[1])

def calc(a, b):
    if b == 0:
        return 0
    elif a % b == 0:
        return a // b
    else:
        return a // b + calc(b, a % b)

print(calc(a, b))