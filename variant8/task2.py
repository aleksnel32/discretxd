#m,n вводим через пробел
M, N = map(int, input().split())

# вводим матрицу через пробел
A = []
for _ in range(M):
    A.append(list(map(int, input().split())))


B = []
for j in range(N):
    column_sum = 0
    for i in range(M):
        column_sum += A[i][j]
    B.append(column_sum)


print(B)
