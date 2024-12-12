

arr = []
# вводить массив через пробел
arr.append(list(map(int, input().split())))

n = len(arr[0])

for i in range(n - 1): #n - 1 потому что первая строка уже введена
    arr.append(list(map(int, input().split())))


row_sums = [sum(row) for row in arr]
print("a:", row_sums)

column_sums = [sum(arr[i][j] for i in range(len(arr))) for j in range(len(arr[0]))]
print("б:", column_sums)
