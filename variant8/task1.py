C = list(map(int, input().split()))
increasing = True # возрастает ли
decreasing = True # убывает ли

for i in range(len(C) - 1):
    if C[i] > C[i + 1]:
        increasing = False
    if C[i] < C[i + 1]:
        decreasing = False

if increasing:
    print("Возрастает")
elif decreasing:
    print("Убывает")
else:
    print("Не упорядочен")
