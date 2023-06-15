hour, mins = map(int, input().split(' '))
plus_min = int(input())

hour += plus_min // 60
mins += plus_min % 60

if mins >= 60:
    mins -= 60
    hour += 1

if hour >= 24:
    hour -= 24

print(hour, mins)
