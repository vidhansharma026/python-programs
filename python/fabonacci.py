num = int(input('enter how many number of fabonnaci print :- '))
a = 0
b = 1

if num > 0:
    for i in range(1,num+1):
        if i == 1:
            print('0',end=',')
        elif i == 2:
            print('1',end=',')
        elif i == num:
            c = a + b
            a = b
            b = c
            print(c,end='')
        else:
            c = a + b
            a = b
            b = c
            print(c,end=',')
else:
    print('enter valid number')