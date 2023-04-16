l = int(input())
a = int(input())
b = int(input())

if l > a or l > b:
    print('UPLOAD ANOTHER')
elif l == a or l == b:
    print('ACCEPTED')
else:
    print('CROP IT')