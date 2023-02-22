n = int(input())
a = []

for i in range(n):
    x = int(input())
    a.append(x)

b = a[::1]
b.sort()

print(b[0], a.index(b[0])) #tìm giá trị nhỏ nhất và vị trí nó
print(b[n - 1], a.index(b[n - 1])) #tìm giá trị lớn nhất và vị trí nó