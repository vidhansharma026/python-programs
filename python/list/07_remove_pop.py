# What is the difference between “remove” and “pop”?

l = ['a','b','c','a','b','c']
# .remove() removes the first instance of a matching object.
l.remove('a')
print(l)
# .pop() removes an object by its index.
l.pop(3)
print(l)
l.pop()
print(l)