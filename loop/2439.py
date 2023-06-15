import sys

T = int(sys.stdin.readline())

for i in range(T):
    print(' ' * int(T - (i + 1)), '*' * int(i + 1), sep='')
