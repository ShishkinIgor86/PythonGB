print('Пограмма находит 2 загаданных натуральных числа X,Y, которые меньше или равны 1000')
P=int(input('Введите числовое значение произведения x*y = '))
S=int(input('Введите числовое значения суммы x+y = '))
if P>1000*1000 and S>1000+1000:
    print('По условию X,Y <=1000 \nзапустите программу еще раз')
    quit()
else:
    if P>S:
        for i in range(1,P):
            for j in range(1,P):
                if i*j==P and i+j==S:
                    X=i
                    Y=j
                else:
                    X=None
                    Y=None
    elif S>P:
        for i in range(1,S):
            for j in range(1,S):
                if i*j==P and i+j==S:
                    X=i
                    Y=j
                else:
                    X=None
                    Y=None
    elif S==P:
        print('К сожалению не могу найти X и Y удовлетворяющих условию')
if X!=None and Y!=None:
    print(f'Первая возможная пара: X={X} b Y={Y}, \nвторая вожможная пара: X={Y} b Y={X}')
else:
    print('К сожалению не могу найти X и Y удовлетворяющих условию')