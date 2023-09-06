# arm strong number 

# num = input('enter any number for check armstrong')
# l = len(num)
# num = int(num)
# temp = num
# rev = 0

# for i in range(1,l+1):
#     store = temp%10
#     rev = rev + store**l
#     temp = temp//10
# if num == rev:
#     print('armstrong')
# else:
#     print('not armstrong')


# armstrong number series

s = int(input('enter starting number :- '))
e = int(input('enter ending number :- '))

for i in range(s,e+1):
    i = str(i)
    l = len(i)
    i = int(i)
    temp = i
    rev = 0
    for j in range(1,l+1):
        store = temp%10
        rev = rev + store**l
        temp = temp//10
    if i == rev:
        print(i,' is armstrong')
    else:
        print(i,' is not armstrong')

