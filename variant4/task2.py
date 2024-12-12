# ввод m n через пробел; M — количество строк, N — количество столбцов.
M, N = map(int, input().split())

#вводить массив через пробел
Q = []
for i in range(M):
    Q.append(list(map(float, input().split())))


Q[0], Q[-1] = Q[-1], Q[0]
for line in Q:
    print(line)
