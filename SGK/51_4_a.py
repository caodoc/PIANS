x = float(input())
y = float(input())

if x ** 2 + y ** 2 <= 1:
    print(x ** 2 + y ** 2)
elif y >= x:
    print(x + y)
else:
    print(0.5)