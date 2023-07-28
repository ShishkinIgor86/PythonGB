def summa(a,b):
    if b==0:
        return a
    else:
        return (1+summa(a,b-1))
    
a=int(input('Введите первое слагаемое: '))
b=int(input('Введите второе слагаемое: '))
print(f'Сумма = {summa(a,b)}')