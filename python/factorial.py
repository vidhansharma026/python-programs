# num = int(input('enter number for factorial :- '))
# fact = 1

# for i in range(1,num+1):
#     fact = fact*i
# print(fact)

# starting and ending for factorial

s = int(input('enter start for factorial'))
e = int(input('enter end for factorial'))

for i in range(s,e+1):
    fact = 1
    for j in range(1,i+1):
        fact = fact*j
    print('factorial of ',i,' is ',fact)