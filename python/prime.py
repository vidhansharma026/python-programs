# print prime number from start to end

# s = int(input('enter starting number for check prime :- '))
# e = int(input('enter ending number for check prime :- '))

# for i in range(s,e+1):
#     if i == 0 or i == 1:
#         print(i,' is not prime')
#     else:
#         for j in range(2,i):
#             if i%j == 0:
#                 print(i,' is not prime')
#                 break
#         else:
#             print(i,' is prime')

# check prime number or not

num = int(input('enter any number for check prime or not :- '))

if num == 0 or num == 1:
    print(num,' is not prime')
else:
    for i in range(2,num):
        if num%i == 0:
            print(num,' is not prime')
            break
    else:
        print(num,' is prime')
