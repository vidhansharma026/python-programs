try:
    a = int(input('enter dividend :- ')) # this gives ValueError if we enter not int value
    # b = input('enter diviser :- ') # this will give TypeError bcz of different types
    b = int(input('enter diviser :- ')) # this gives ZeroDivisionError when we enter zero as diviser
    v = a/b 
    # v = a/b: # this will give SyntaxError
    # prit(v) # this gives NameError
    print(v)
    # for i in range(5):
    # print(i)  # IndentationError is raised at ""compile"" time. try-except can only handle exceptions that are raised at run time.
except ZeroDivisionError:
    print('this value is not divided by zero')
except ValueError:
    print('this value is not valid')
except NameError:
    print('this name is not defined')
except SyntaxError:
    print('this syntax is not valid')
except TypeError:
    print('different types are not valid')
except KeyboardInterrupt:
    print('dont interrput')
except Exception as e:
    print(e)
    print(type(e))

