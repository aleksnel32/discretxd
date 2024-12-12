import random

5
A = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]


print("Исходная матрица:")
for row in A:
    print(row)

for i in range(10):
    for j in range(i + 1, 10):  
        A[i][j], A[j][i] = A[j][i], A[i][j]


print("Транспонированная матрица:")
for row in A:
    print(row)
