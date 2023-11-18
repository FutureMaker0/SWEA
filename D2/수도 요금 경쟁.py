import sys
sys.stdin = open("input/수도 요금 경쟁.txt", "r")

T = int(input())
for tc in range(1, T+1):
    li = list(map(int, input().split()))
    P = li[0]
    Q = li[1]
    R = li[2]
    S = li[3]
    W = li[4]
    # print(P, Q, R, S, W)

    # case a
    # 리터당 P원
    # case b
    # 기본요금 Q, R이하인 경우 기본요금만, 초과하면 리터당 P+S원으로 계산

    com_a = W * P
    if W <= R:
        com_b = Q
    else:
        com_b = Q + ((W-R)*(S))

    # print(com_a, com_b)
    print(f'#{tc} {min(com_a, com_b)}')
