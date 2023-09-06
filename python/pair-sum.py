# l = [2,7,4,5,9,1] 
# target = 9

# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j] == target:
#             print(i,j)

l = [2,7,4,5,9,1] 
t = 9
s1 = set()

for i in l:
    s = t-i
    if s in l:
        s1.add(l.index(s))
        s1.add(l.index(i))
print(s1)