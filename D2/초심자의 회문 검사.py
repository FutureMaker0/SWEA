import sys
sys.stdin = open("input/초심자의 회문 검사.txt", "r")

T= int(input())
for tc in range(1, T+1):
    N = str(input())

    # print(N[0:len(N)//2])
    # 지금 홀수일때만 고려되어 있음, 문자열 길이가 짝수일 때 오류
    if len(N) % 2 != 0:
        front = N[0:len(N)//2]
        end = N[len(N)//2 + 1:]
        reverse_end = end[::-1]
    else:
        front = N[0:len(N) // 2]
        end = N[len(N) // 2:]
        reverse_end = end[::-1]
    # print(N, front, end, reverse_end)

    if front == reverse_end:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')
