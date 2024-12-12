#М не требуется, вводить сразу массив
#вводить массив через пробел
B = list(map(int, input().split()))
imin = B.index(min(B))

B.pop(imin)
print(B)
