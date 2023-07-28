
def prod(a,b):
    if b==1:
        return a
    elif b==0:
        return 1
    else:
        return(a* prod(a,b-1))

a=int(input('Введите основание степени: '))
b=int(input('Введите показатель степени: '))
print(f'{a} в степени {b} = {prod(a,b)}')