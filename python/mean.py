# mean or average
n = int(input("Number of Elements to take average of: "))  
l = []
for i in range(1,n+1):
    e = int(input('enter elements :- '))
    l.append(e)
avg = sum(l)/n
print('average or mean is ',avg)