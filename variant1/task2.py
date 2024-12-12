# сначала ввод n
n = int(input())

arr = []
# вводить массив через пробел
arr.append(list(map(int, input().split())))


for i in range(n - 1): #n - 1 потому что первая строка уже введена
    arr.append(list(map(int, input().split())))


result = 0
for i in range(len(arr)):
    #arr[i][i] это центральный элемент
    if 25 <= arr[i][i] <= 115:
        result += arr[i][i]

print(result)