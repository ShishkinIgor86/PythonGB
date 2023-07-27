from random import randint
import os
clear = lambda: os.system('cls')
res = int(input('Введите кол-во кустов: '))
kust = list(randint(1, 10) for i in range(res))
max=kust[-1]+kust[0]+kust[1]

if max<kust[len(kust)-1]+kust[len(kust)-2]+kust[0]:
    max=kust[len(kust)-1]+kust[len(kust)-2]+kust[0]

for i in range(1,len(kust)-1):
    if max<kust[i-1]+kust[i]+kust[i+1]:
        max=kust[i-1]+kust[i]+kust[i+1]
        
clear()
print(f'{res}->{kust}')
print(max)