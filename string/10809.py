s = input()
alphabets = [-1 for i in range(27)]

for i in range(len(s)):
    if alphabets[ord(s[i]) - 97] == -1:
        alphabets[ord(s[i]) - 97] = i


for i in range(26):
    print(alphabets[i], end=' ')