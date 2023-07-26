from random import randint
import os
clear = lambda: os.system('cls')
kust = list(randint(1, 10) for i in range(int(input('Введите кол-во кустов: '))))
print(kust)
a = int(input('Введите № куста: '))
res = 0
if a == 1:
    res = kust[0] + kust[1] + kust[-1]
elif a == len(kust):
    res = kust[-2] + kust[-1] + kust[0]
else:
    res = kust[a-1] + kust[a-2] + kust[a]
clear()
print(f'{a}->{kust}')
print(res)