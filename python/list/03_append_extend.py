# Is a list mutable?
# yes

l = [1]
print(id(l),':',l)

# .append() adds an object to the end of a list.
l.append([2,3])
# .extend() adds each value from a 2nd list as its own element. So extending a list with another list combines their values.
l.extend([4,5])
print(id(l),':',l)