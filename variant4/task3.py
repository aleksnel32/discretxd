def f(a1, d, n):
    if n == 1:
        return a1
    return f(a1, d, n - 1) + d

#n - номер нужного члена арифметической прогрессии
#a1 - первый член прогрессии
#d - шаг

# а1, d и n через пробел
a1, d, n = list(map(int, input().split()))

print(f(a1, d, n))