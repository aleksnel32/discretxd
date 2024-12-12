def f(a1, q, n):
    if n == 1:
        return a1
    return f(a1, q, n - 1) + a1 * q ** (n - 1)

#n - номер нужного члена геом прогрессии
#a1 - первый член прогрессии
#q - шаг

# а1, q и n через пробел
a1, q, n = list(map(int, input().split()))

print(f(a1, q, n))