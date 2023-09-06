num = int(input('enter any number'))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print('*',end="")
#     print("")

# *
# **
# ***
# ****
# *****

# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print('j',end="")
#     print("")

# 1
# 12
# 123
# 1234
# 12345

# for i in range(num,0,-1):
#     for i in range(1,i+1):
#         print('*',end="")
#     print('')

# *****
# ****
# ***
# **
# *

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
#     for j in range(1,i*2):
#         print(j,end='')
#     print()

# 1
# 123
# 12345
# 1234567
# 123456789

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
#     for j in range(num+1-i,num+1):
#         print(j,end='')
#     print()

# 5
# 45
# 345
# 2345
# 12345

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
#     for j in range(i,0,-1):
#         print(j,end='')
#     print()

# 1
# 21
# 321
# 4321
# 54321

for i in range(1,num+1):
    for j in range((num*2-1)-2*i,0,-2):
        print(j,end='')
    print()