#не совсем понял чо там имеется в виду но вроде так
def f(s, n):
    if n == 0:
        return 1
    elif n > 0:
        return s * f(s, n-1)
    else:
        return 1 / f(s, -n)

print(f(2, 3))