T = 10
for test_case in range(1, T + 1):
    N = int(input())
    li = list(map(int, input().split())) # 빌딩리스트
    # print(li)

    cnt = 0
    for i in range(2, N-2):
        if li[i] > li[i-2] and li[i] > li[i-1] and li[i] > li[i+1] and li[i] > li[i+2]:
            d1 = li[i] - li[i-2]
            d2 = li[i] - li[i-1]
            d3 = li[i] - li[i+1]
            d4 = li[i] - li[i+2]

            min_gap = d1
            for d in [d1, d2, d3, d4]:
                if d < min_gap:
                    min_gap = d

            cnt += min_gap

    print("#{} {}".format(test_case, cnt))
