list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

croatia_word = input()

for i in list:
    if croatia_word.__contains__(i):
        croatia_word = croatia_word.replace(i, 'ㅋ')

print(len(croatia_word))