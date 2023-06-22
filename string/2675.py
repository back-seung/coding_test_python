T = int(input())

for _ in range(T):

    repeat, S = input().split()

    for i in range(len(S)):

        print(S[i] * int(repeat), end='')
    print()