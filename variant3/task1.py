#М не требуется вводить, сразу массив
#через пробел элементы массива вводить
B = list(map(int, input().split()))


def maxv(list):
    result = 0
    for item in list:
        if result < item:
            result = item
    return result


def minv(list):
    result = 99999999
    for item in list:
        if result > item:
            result = item
    return result

imin = B.index(minv(B))
imax = B.index(maxv(B))

B[imin], B[imax] = B[imax], B[imin]

print(B)
