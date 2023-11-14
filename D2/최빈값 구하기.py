T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    S = int(input())
    temp = [0] * 10
    li = list(map(int, input().split()))
    # print(li)
    for i in li:
        temp[i] += 1
    print(temp)

    same_freq = []
    for j in range(len(temp)):
        if temp[j] == max(temp):
            # print(j)
            same_freq.append(j)

    print("#"+str(test_case), max(same_freq))
