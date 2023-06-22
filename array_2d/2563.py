square = [[0 for j in range(101)] for i in range(101)]

papers = int(input())

for _ in range(papers):
    W, H = list(map(int, input().split()))

    for i in range(W, W + 10):
        for j in range(H, H + 10):
            square[i][j] = 1

count = 0
for i in square:
    count += i.count(1)

print(count)
