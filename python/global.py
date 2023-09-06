def func():
   global value
   value = "Local"
   print(value)
   
value = "Global"
func()
print(value)

#Local