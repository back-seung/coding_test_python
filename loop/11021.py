import sys

T = int(sys.stdin.readline())

for i in range(T):
    print('Case #', i + 1, ': ', sum(map(int, sys.stdin.readline().split(' '))), sep='')
