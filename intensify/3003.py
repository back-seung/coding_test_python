# 킹, 퀸, 나이트, 비숍, 룩, 폰 [1,1,2,2,2,8]

count_list = [1, 1, 2, 2, 2, 8]

given_list = list(map(int, input().split(' ')))

for i in range(len(count_list)):
    given_list[i] = count_list[i] - given_list[i]


for i in given_list:
    print(i, end=' ')
