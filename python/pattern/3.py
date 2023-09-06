num = int(input('enter the no of rows'))

# for i in range(1,num+1):
#     for j in range(1,i*2):
#         print('*',end='')
#     print()

# *
# ***
# *****
# *******
# *********

# for i in range(1,num+1):
#     for j in range(1,i*2,2):
#         print(j,end='')
#     print()

# 1
# 13
# 135
# 1357
# 13579

# for i in range(1,num+1):
#     for j in range(2,i*2+1,2):
#         print(j,end='')
#     print()

# 2
# 24
# 246
# 2468
# 246810

# for i in range(1,num+1):
#     for j in range(1,num+2-i):
#         print(j,end='')
#     print()

# 12345
# 1234
# 123
# 12
# 1

# for i in range(1,num+1):
#     for j in range(num,num-i,-1):
#         print(j,end='')
#     print()

# 5
# 54
# 543
# 5432
# 54321

# for i in range(1,num+1):
#     for j in range(i*2-1,0,-2):
#         print(j,end='')
#     print()

# 1
# 31
# 531
# 7531
# 97531

# for i in range(1,num+1):
#     for j in range(i,0,-1):
#         print(j,end='')
#     print()

# 1
# 21
# 321
# 4321
# 54321

# for i in range(1,num+1):
#     for j in range(1,num+1-i):
#         print(' ',end='')
#     for k in range(1,i+1):
#         print('* ',end='')
#     print()

#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# for i in range(1,num+1):
#     for j in range(1,num+2-i):
#         print(i,end='')
#     print()

# 11111
# 2222
# 333
# 44
# 5

# for i in range(1,num+1):
#     for j in range(num+1-i,0,-1):
#         print(j,end='')
#     print()

# 54321
# 4321
# 321
# 21
# 1

# for i in range(num,0,-1):
#     for j in range(1,i+1):
#         print(i,end='')
#     print()

# 55555
# 4444
# 333
# 22
# 1
