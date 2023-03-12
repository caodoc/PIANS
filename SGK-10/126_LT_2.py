s = input()

r = s.split()

print("Ho va ten dem:",end = " ")
for i in range(len(r) - 1):
    print(r[i],end = " ")
print()
print("Ten:",r[len(r) - 1])