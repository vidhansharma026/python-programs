from sys import exit

class Add:
    def result(self, a, b):
        print('Addition is :- ', a+b)
        exit()
        # exit()  # we can directly use or import them
        # quit()  # quit() method is use to terminate the execution of programme

class Multi(Add):
    def result(self, a, b):
        super().result(10,20)
        print('Multiplication is :- ', a*b)

obj = Multi()
obj.result(10,20)