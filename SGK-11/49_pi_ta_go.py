a = float(input())
b = float(input())
c = float(input())

if a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or c ** 2 + a ** 2 == b ** 2:
    print("YES")
else:
    print("NO")