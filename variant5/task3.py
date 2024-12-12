#функция для нахождения n-ного члена прогрессии
def arProg(a1, d, n):
    if n == 1:
        return a1
    return arProg(a1, d, n - 1) + d

def arSum(a1, d, n):
    if n == 1:
        return a1
    return arSum(a1, d, n - 1) + arProg(a1, d, n)

#n - номер нужного члена арифметической прогрессии
#a1 - первый член прогрессии
#d - шаг

# а1, d и n через пробел
a1, d, n = list(map(int, input().split()))

print(arSum(a1, d, n))