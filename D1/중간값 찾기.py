# import sys
# sys.stdin = open("input2.txt", "r")

T = int(input())
li = list(map(int, input().split()))

li.sort()

print(li[len(li)//2])
