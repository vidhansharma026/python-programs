# How to iterate over 2+ lists at the same time

name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
animal = ['Cat', 'Dog', 'Fish', 'Goat']
age = [1, 2, 2, 6]

z = zip(name,animal,age)

for i,j,k in z:
    print('%s the %s is %d' % (i,j,k))

# for name,animal,age in z:
#     print('%s the %s is %d' % (name,animal,age))
