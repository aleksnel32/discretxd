#вводить через пробел
a = list(map(int, input().split()))
n = len(a) - 1

resultA = a.copy()

for i in range(len(a)//2):
    resultA[i] = a[n - i]
    resultA[n - i] = a[i]

print(resultA)

resultB = a.copy()

for i in range(0, len(a) - 1, 2):
    resultB[i] = a[i + 1]
    resultB[i + 1] = a[i]

print(resultB)
