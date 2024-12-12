
even_numbers = []
for i in range(2, 201, 2):
    even_numbers.append(i)


B = [[0] * 10 for _ in range(10)]

index = 0
for col in range(10):
    for row in range(10):
        B[row][col] = even_numbers[index]
        index += 1

for row in B:
    print(row)
