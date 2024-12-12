def f(a, n):
    if n == 0:
        return 1
    return a * f(a, n - 1)

# а и n через пробел
a, n = list(map(int, input().split()))
print(f(a, n))