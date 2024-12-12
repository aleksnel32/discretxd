#вводить массив через пробел
W = list(map(int, input().split()))
W = [x for x in W if x != 0]
print(W)
