import sys
sys.stdin = open("input1.txt","r")

T = int(input())

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for tc in range(1, T+1):
    N = int(input())

    arr = [[0] * N for _ in range(N)]
    i, j, dr, cnt = 0, 0, 0, 1

    arr[i][j] = cnt
    cnt += 1

    while cnt <= N*N:
        ni, nj = i + di[dr], j + dj[dr]
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0:
            i, j = ni, nj
            arr[i][j] = cnt
            cnt += 1
        else:
            dr = (dr+1) % 4

    print(f'#{tc}')
    for list in arr:
        print(*list)
