n,m=map(int,input('Введите размерность первого и второго набора целых чисел через пробел: ').split())

first_l=list(map(int,input('Первая последовательность (вводится через пробел): ').split()))
if len(first_l)!=n:
    print(f'Вы ввели не {n} элементов первого набора целых чисел')
    quit()
second_l=list(map(int,input('Вторая последовательность (вводится через пробел): ').split()))
if len(second_l)!=m:
    print(f'Вы ввели не {m} элементов второго набора целых чисел')
    quit()
first=set(first_l)
second=set(second_l)
l_f=sorted(first&second)
print(' '.join(map(str, l_f)))
