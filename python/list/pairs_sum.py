l = [1,2,3,4,5,6,7,8,9,]
s = 10
res = []

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i] + l[j] == s:
            res.append((l[i],l[j]))
print(res)