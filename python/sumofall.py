# start = int(input('enter start number for sum :- '))
# last = int(input('enter last number for sum :- '))
# print(sum(range(start,last)))

start = int(input('enter start number for sum :- '))
last = int(input('enter last number for sum :- '))
sum = 0
for i in range(start,last+1):
    sum = sum + i
print(sum)
