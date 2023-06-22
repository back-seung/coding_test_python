rows, cols = map(int, input().split(' '))

A = [[0 for j in range(cols)] for i in range(rows)]
B = [[0 for j in range(cols)] for i in range(rows)]

for i in range(rows):
    elems = list(map(int, input().split(' ')))
    for j in range(cols):
        A[i][j] = int(elems[j])

for i in range(rows):
    elems = list(map(int, input().split(' ')))
    for j in range(cols):
        B[i][j] = int(elems[j])

for i in range(rows):
    for j in range(cols):
        A[i][j] = A[i][j] + B[i][j]
        print(A[i][j], end=' ')
    print()


