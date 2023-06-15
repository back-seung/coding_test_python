import math

total_cost = int(input())
stuffs = int(input())
valid_total = 0

for i in range(stuffs):
    valid_total += math.prod(map(int, input().split(' ')))

if total_cost == valid_total:
    print('Yes')
else:
    print('No')
