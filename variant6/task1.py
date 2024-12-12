import random

N = 10
A = [random.randint(-10, 10) for _ in range(N)]
maxv = -99999999999

for i in range(N - 1):
    product = A[i] * A[i + 1]
    if product > maxv:
        maxv = product

print(A)
print(maxv)
