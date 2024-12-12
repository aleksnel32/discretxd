# вводим n
n = int(input("Введите размерность n: "))

chessboard = [[0] * n for _ in range(n)]


if n % 2 == 0:
    for i in range(n):
        for j in range(n):
            chessboard[i][j] = (i + j) % 2
else:
    for i in range(n):
        for j in range(n):
            chessboard[i][j] = (i + j + 1) % 2



for row in chessboard:
    print(" ".join(map(str, row)))
