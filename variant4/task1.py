#М не требуется, вводить сразу массив
#вводить массив через пробел


def minv(list):
    result = 99999999
    for item in list:
        if result > item:
            result = item
    return result



B = list(map(int, input().split()))
print(minv(B))
imin = B.index(minv(B))

B.pop(imin)
print(B)
