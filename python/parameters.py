# Positional parameters or arguments
def one(a,b):  #parameters
    sum = a+b
    return sum

print(one(3,3)) #arguments

# Default parameters or arguments
def two(a1, b1=3):  #parameters (we can not give default parameter first)
    sum1 = a1+b1
    return sum1

print(two(3,4)) #arguments

# keyword parameters or arguments
def three(a2,b2):  #parameters
    sum2 = a2+b2
    return sum2

print(three(b2=4,a2=4)) #arguments

# variable length parameters or arguments
def four(*args):  #parameters
    sum3 = 0
    for i in args:
        sum3 =sum3 + i
    return sum3

print(four(3,3,3)) #arguments

# keyword length parameters or arguments
def five(**kwargs):
    total_sum = 0
    for key, value in kwargs.items():
        total_sum += value
    return total_sum

# Call the function with keyword arguments
result = five(num1=3, num2=5, num3=10)
print("Sum:", result)
#arguments

