Nums = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', "WXYZ"]

word = list(input())
count = 0

for i in word:
    for j in Nums:
        if i in j:
            count += (Nums.index(j) + 3)
print(count)