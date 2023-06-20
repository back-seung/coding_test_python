N = int(input())
scores = list(map(int, input().split()))
M = max(scores)
average = 0

for i in range(N):
    average += (scores[i]/M) * 100

print(average / N)

