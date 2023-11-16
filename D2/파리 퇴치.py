T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    # N*N개 만큼 arr 입력
    arr = []
    for _ in range(N):
        li = list(map(int, input().split()))
        arr.append(li)
    # print(arr)

    # 이렇게 하면 1번 예제만 맞는다. 2x2일때만...
    max = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            # sum_val = arr[i][j] + arr[i][j+(M-1)] + arr[i+(M-1)][j] + arr[i+(M-1)][j+(M-1)]

            sum_val = 0
            for m in range(i, i+M):
                for n in range(j, j+M):
                    sum_val += arr[m][n]

                    if sum_val > max:
                        max = sum_val

    print(f'#{tc} {max}')
