from functools import lru_cache

@lru_cache(None) #кеширование прошлых результатов
def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

n = int(input())

for i in range(1, n + 1):
    print(factorial(i), end=' ')
