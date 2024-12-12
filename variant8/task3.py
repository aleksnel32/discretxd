def f(function, a, b, e):

    center = (a + b) / 2

    if abs(function(center)) < e:
        return center

    if function(a) * function(center) < 0:
        return f(function, a, center, e)
    else:
        return f(function, center, b, e)


#a, b - границы
#e - точность


# a, b и e через пробел
a, b, e = list(map(float, input().split()))

import math
# нужная функция можно указать тригонометрические к примеру math.sin math.cos и др
function = math.sin

print(f(function, a, b, e))