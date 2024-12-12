import random
arr = []
# вводить массив через пробел

for i in range(10): 
    arr.append(list(map(float, input().split())))

for i, row in enumerate(arr):
    neg_count = sum(1 for x in row if x < 0)
    if neg_count > 5:
        print(i + 1)
