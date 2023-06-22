arr = [list(map(str, input())) for i in range(5)]

max_elems = 0
for i in range(len(arr)):
    if max_elems < len(arr[i]):
        max_elems = len(arr[i])

for i in range(max_elems):
    for j in range(5):
        try:
            print(arr[j][i], end='')
        except IndexError:
            continue

