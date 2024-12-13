w = []
# вводить через пробел

for i in range(5):
    r = list(map(int, input().split()))
    if (i+1) % 2 == 0:
        for i, element in enumerate(r):
            if abs(element) < 45625:
                r[i] = 0
    w.append(str(r))

for line in w:
    print(line)
