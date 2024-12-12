
#вводить через пробел
arr = map(float, input().split())

negativeArr = []

for element in arr:
    if element <= 0:
        negativeArr.append(element)
    else:
        print(element, end = ' ')

print(negativeArr[::-1][:3])