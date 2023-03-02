s1 = input()
s2 = input()

n = len(s2) // 2
s3 = ""

for i in range(0,n):
    s3 += s2[i]
for i in s1:
    s3 += i
for i in range(n,len(s2)):
    s3 += s2[i]

print(s3)