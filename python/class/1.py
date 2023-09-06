class Demo:
    a = 'car' # class variable or static variable
    def __init__(self):
        self.model = 188 # instance variable
    def show(self): # instance method
        print(self.model)
        print(self.a)
        self.a = 'cars'
        print(self.a)
    @classmethod
    def cl_fn(cls):
        print('this is class fun')
    
# obj = Demo() # obj creation or instance creation
# print(obj.model)
# print(obj.a)
# obj.show()
# obj.cl_fn()

# print(Demo.a)
# Demo.show(self)