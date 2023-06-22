word = input().lower()
word_unique = list(set(word))
count_list = []

for i in word_unique:
    count_list.append(word.count(i))

if count_list.count(max(count_list)) >= 2:
    print('?')
else:
    print(word_unique[count_list.index(max(count_list))].upper())
