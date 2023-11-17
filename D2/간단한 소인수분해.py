import sys
sys.stdin = open("간단한 소인수분해.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    dict = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0}

    # 특정 i로 나눠지면 걔로 계속 돌려야 한다.
    for i in dict:
        # print(i, N)
        while N > 0 and N % i == 0:
            dict[i] += 1
            N = N // i

    print('#{} {} {} {} {} {}'.format(tc, *list(dict.values())))


