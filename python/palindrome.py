# check palindrome number

# num = input('enter a num for check palindrome or not :- ')
# l = len(num)
# num = int(num)
# store,temp,rev = 0,num,0 

# for i in range(1,l+1):
#     store = temp % 10
#     rev = rev*10 + store
#     temp = temp // 10
# if rev == num :
#     print('palindrome')
# else:
#     print('not palindrome')


# palindrome series

s = int(input('enter starting for palindrome :- '))
e = int(input('enter ending for palindrome :- '))

for i in range(s,e+1):
    temp = i
    store,rev = 0,0
    i = str(i)
    l = len(i)
    i = int(i)
    for j in range(1,l+1):
        store = temp%10
        rev = rev*10 + store
        temp = temp // 10
    if rev == i:
        print(i,' is palindrome')
    else:
        print(i,' is not palindrome')
