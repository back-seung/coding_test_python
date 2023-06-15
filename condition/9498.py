import random

def get_score(score):
    if score >= 90:
        return 'A'
    elif score < 90 and score >= 80:
        return 'B'
    elif score < 80 and score >= 70:
        return 'C'
    elif score < 70 and score >= 60:
        return 'D'
    else:
        return 'F'


def test_get_score():
    for i in range(10):
        score = random.randint(1, 100)
        print('점수는 ', score, '점. \n성적은 ', get_score(score), '입니다')


print(get_score(int(input())))


