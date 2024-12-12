#хз вроде все правильно сделал (возможно я где то налажал)

#N не требуется, вводить сразу массив
#вводить массив через пробел
me = list(map(float, input().split()))

MU = sum(me) / len(me)

DU = sum((Ui - MU) ** 2 for Ui in me) / (len(me) - 1)

print(MU)
print(DU)
