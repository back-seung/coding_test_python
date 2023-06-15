import sys

T = int(sys.stdin.readline())
list = list(map(int, sys.stdin.readline().split(' ')))
count_value = int(sys.stdin.readline())

print(list.count(count_value))