def is_leaf_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 400 == 0):
        print(1)
    else:
        print(0)

is_leaf_year(2012)
