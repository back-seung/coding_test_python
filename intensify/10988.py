# 팰린드롬 - 뒤집어도 같게 읽히는 문자

S = input()

if S == S[::-1]:
    print(1)
else:
    print(0)