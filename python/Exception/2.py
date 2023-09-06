try:
    val = input('enter name :- ')
    if val == "vidhan":
        raise Exception('name is not define')
except Exception as e:
    print(e)
    print(type(e))