import sys

N, M = map(int, sys.stdin.readline().split(' '))
list = [i + 1 for i in range(N)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    temp = list[i-1:j]
    temp.reverse()
    list[i-1:j] = temp

for i in range(len(list)):
    print(list[i], end='')