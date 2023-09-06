def new_add(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

@new_add
def add(a,b):
    print(a/b)
# div1 = new_add(add)
add(2,4)
