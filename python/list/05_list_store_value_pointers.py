# Do python lists store values or pointers?
# Python lists don’t store values themselves. They store pointers to values stored elsewhere in memory. This allows lists to be mutable.

print(id(1))
print(id(2))

l = [1,2,3]
print(id(l))
print(id(l[0]))
print(id(l[1]))
print(id(l[2]))
