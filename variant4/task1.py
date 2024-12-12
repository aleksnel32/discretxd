#М не требуется, вводить сразу массив
#вводить массив через пробел


def minv(list):
    result = 9999999
    for item in list:
        if result < item:
            result = item
    return item

B = list(map(int, input().split()))
imin = B.index(minv(B))

B.pop(imin)
print(B)
