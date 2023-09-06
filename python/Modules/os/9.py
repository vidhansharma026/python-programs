import os 

f = os.walk('.')
for i in f:
    print(i)

c = os.chdir('D:/python/Modules/')
f = os.walk('.')
for i in f:
    print(i)