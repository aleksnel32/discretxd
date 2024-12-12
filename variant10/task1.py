#вводить массив 1 через пробел
A = list(map(int, input().split()))
#вводить массив 2 через пробел
B = list(map(int, input().split()))

S = 0
for i in range(len(A)):
    S += A[i] * B[i]

print(S)
