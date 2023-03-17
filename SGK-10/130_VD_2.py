def num(x):
    cnt = 0
    for i in x:
        if i >= '0' and i <= '9':
            cnt += 1
    return cnt

def cntchr(x):
    cnt = 0
    for i in x:
        if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
            cnt += 1
    return cnt

s = input()

print("So chu so:",num(s))
print("So ki tu:",cntchr(s))