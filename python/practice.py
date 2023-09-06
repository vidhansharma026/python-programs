num = input('enter any num : ')
l = len(num)
num = int(num)
temp = num
rev = 0

for i in range(1,l+1):
    store = temp%10
    rev = rev + store**l
    temp = temp//10
print(rev)