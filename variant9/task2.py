# вводим n
n = int(input("Введите размерность n: "))

chessboard = [[0] * n for _ in range(n)]


for i in range(n):
    for j in range(n):
        #n % 2 в скобке нужна чтобы сдвигать сетку на 1 при нечетном варианте
        chessboard[i][j] = (i + j + n % 2) % 2 



for row in chessboard:
    print(" ".join(map(str, row)))
