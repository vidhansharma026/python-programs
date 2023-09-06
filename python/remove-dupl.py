l = [2,2,4,4,6,7,8,9,3,5,6,8,9,2,2]
print(id(l))

i = 0
while i < len(l):
    if l.count(l[i]) > 1:
        l.pop(i)
    else:
        i +=1

print(l)
print(id(l))