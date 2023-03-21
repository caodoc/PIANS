def change(s, c):
    if (c == 0):
        return s.upper()
    return s.lower()

s = input()
c = int(input())
print(change(s, c))