a1=int(input('Введите первый член арифметической прогрессии a1: '))
d=int(input('Введите разность арифметической прогрессии d: '))
n=int(input('Введите количество членов арифметической прогрессии: '))
ar_pr=[a1+(n-1)*d for n in range(1,n+1)]
print(*ar_pr, sep=', ')