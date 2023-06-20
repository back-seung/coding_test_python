list = []
for _ in range(28):
    list.append(int(input()))

list.sort()

for i in range(1, 31):
    if not list.__contains__(i):
        print(i)

