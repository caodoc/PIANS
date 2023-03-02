s = input()
ck = False

for i in s:
    if (i >= "0" and i <= "9"):
        ck = True
        break

if (ck == True):
    print("YES")
else:
    print("NO")