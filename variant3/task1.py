#М не требуется вводить, сразу массив
#через пробел элементы массива вводить
B = list(map(int, input().split()))

imin = B.index(min(B))
imax = B.index(max(B))

B[imin], B[imax] = B[imax], B[imin]

print(B)
