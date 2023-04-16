n = int(input())
s = input()
s = s.split()

Max = -1000
Min = 1000

for i in range(n):
    t = int(s[i])
    Max = max(Max, t)
    Min = min(Min, t)
    
print(abs(Max - Min))