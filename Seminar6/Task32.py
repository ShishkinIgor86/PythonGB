import random
n=int(input('Введите количество элементов в массиве: '))
array=[random.randint(1,20) for i in range(n)]
print('Сформированный массив: ', end='')
print(*array, sep=' ')
min_c=int(input('Введите нижнюю границу заданного диапазона: '))
max_c=int(input('Введите верхнюю границу заданного диапазона: '))
if min_c>max_c:
    print('Просьба запустите программу заново, нижняя граница не может быть больше верхней.')
else:
    print(f'Найдем и выведем все индексы значений которые принадлежат промежутку заданному диапазоном [{min_c},{max_c}]')
    indexes=[]
    for i in range(n):
        if array[i]>=min_c and array[i]<=max_c:
            indexes.append(i)
    if len(indexes)==0:
        print('Никакие значения не попали в выбранный диапазон, не могу вывести индексы')
    else:
        print('Индексы интересующих элементов равны: ', end='')
        print(*indexes, sep=',')