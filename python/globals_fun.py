a = 50

def display():
    a = 100
    print('Local variable :- ', a)
    store = globals()['a']
    print('Global variable :- ', store)
    store = 40
    print('Store variable :- ', store)

display()
print('Global variable :- ', a)

g = 10

def show():
    global g
    print('Global variable in fun:- ', g)

show()
print('Global variable :- ', g)

