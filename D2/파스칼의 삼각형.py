T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = []
    for i in range(N):
        list = []
        for j in range(i+1):
            if j == 0 or j == i:
                list.append(1)
            else:
                list.append(arr[i-1][j-1] + arr[i-1][j])

        arr.append(list)

    print(f'#{tc}')
    for lst in arr:
        print(*lst)

