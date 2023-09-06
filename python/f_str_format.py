# f string and format 
name = input("enter your first name ")
lname = input("enter your last name ")

print(f"hi,my name is {name} and last name is {lname}")
print(("hello my name is {} and last name is {}").format(name,lname))
print("Hii, my name is %s and my last name is %s"%(name,lname))