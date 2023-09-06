'''
random() - This instruction gives a floating-point value ranging from 0 to 1.
uniform(X, Y) - This function gives a floating-point value in the X and Y range.
randint(X, Y) - This function gives a random integer between X and Y values.
'''

import random
r = random.random()  # it gives 
u = random.uniform(1, 10)
ri = random.randint(1,10)
print(r)
print(u)
print(ri)