#вводить массив через пробел
B = list(map(int, input().split()))
arr = []
for i in range(len(B)):
    for j in range(i + 1, len(B)):
        if B[i] == B[j]:
            arr = [i, j]
            break
    if arr:
        break

print(arr[0], arr[1])
