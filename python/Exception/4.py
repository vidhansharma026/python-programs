try:
    a = int(input('enter any number between 10 '))
    if a > 10:
        raise Exception('wrong input')
except Exception as e:
    print(e)
else:
    print('this is your lucky num')
finally:
    print('your done')