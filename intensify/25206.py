score_table = dict()

score_table['A+'] = 4.5
score_table['A0'] = 4.0
score_table['B+'] = 3.5
score_table['B0'] = 3.0
score_table['C+'] = 2.5
score_table['C0'] = 2.0
score_table['D+'] = 1.5
score_table['D0'] = 1.0
score_table['F'] = 0.0
score_table['P'] = 0.0
avg = 0
sum = 0
for i in range(20):
    score = input().split(' ')
    if score[2] == 'P' or score[2] == 'D':
        continue
    else:
        avg += float(score[1]) * float(score_table.get(score[2]))
        sum += float(score[1])
print(float(avg / sum))