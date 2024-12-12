# ввод N
N = int(input()) 

# ввод P через пробел
P = []
for _ in range(N):
    P.append(list(map(float, input().split())))


sum_main_diag = sum(P[i][i] for i in range(N))
sum_secondary_diag = sum(P[i][N - 1 - i] for i in range(N))


if sum_main_diag > sum_secondary_diag:
    print("Сумма главной диагонали больше.")
elif sum_main_diag < sum_secondary_diag:
    print("Сумма побочной диагонали больше.")
else:
    print("Суммы главной и побочной диагоналей равны.")
