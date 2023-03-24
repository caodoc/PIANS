import datetime

def calc(d, m, y):
    ngay = int(d)
    thang = int(m)
    nam = int(y)
    check = True
    try:
        temp = datetime.datetime(nam,thang,ngay)
    except:
        check = False
    if (check):
        print("Hop le")
    else:
        print("Khong hop le")

    return

s = input()
s = s.split()
day = s[0]
month = s[1]
year = s[2]

calc(day, month, year)