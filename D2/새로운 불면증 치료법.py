T = int(input())
for tc in range(1, T+1):
    N = int(input())
    list = [0] * 10

    cnt = 0
    i = 1
    while 0 in list:
        curr_N = i * N
        # print(curr_N)

        for elem in str(curr_N):
            list[int(elem)] = 1

        i += 1
        cnt += 1
        # print(list, cnt)

    # print(list, cnt)
    # print(' ')

    print(f'#{tc} {N * cnt}')
