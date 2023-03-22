s = input()

n = len(s)
check = True

for i in range(n//2):
    if (s[i] != s[n - i - 1]):
        check = False
        break

if (check == True):
    print("YES")
else:
    print("NO")