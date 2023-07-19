print('0 - решка, 1 - орел')
n=int(input('Введите количество монет: '))
orel=0
reshka=0
for i in range(n):
    m=int(input(f'Введите расположение {i+1} монеты: '))
    if m==0:
        reshka+=1
    else:
        orel+=1
if reshka>orel:
    print(f'Вам необходимо перевернуть {n-reshka} монет')
elif orel>reshka:
    print(f'Вам необходимо перевернуть {n-orel} монет')
else:
    print(f'Вам необходимо перевернуть {n-reshka} монет')
