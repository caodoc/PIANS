s1 = input()
s2 = input()

n = len(s2) // 2
s3 = ""

s3 += s2[:n]
s3 += s1
s3 += s2[n:len(s2)]

print(s3)