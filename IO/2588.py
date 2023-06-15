A = int(input())
B = int(input())

list_of_b = list(map(int, str(B)))

print(A * list_of_b[2])
print(A * list_of_b[1])
print(A * list_of_b[0])
print(A * B)
