# import sys
# sys.stdin = open("연월일달력.txt", "r")

T = int(input())

for tc in range(1, T+1):
    date = str(input())
    # print(date)

    year = date[0:4]
    month = date[4:6]
    day = date[6:]

    # print(year, month, day)
    # print(year, int(month), int(day))

    dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    if 0 < int(month) <= 12 and int(day) <= dict[int(month)]:
        print('#{} {}'.format(tc, year + '/' + month + '/' + day))
    else:
        print('#{} {}'.format(tc, -1))
