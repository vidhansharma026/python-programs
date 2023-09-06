import re

epat = '[a-z]{1,}?[0-9]{1,}[@][a-z]{3,}[.][a-z]{2,3}'
email = input('enter valid email address :- ')
# email = 'vidhansharma026@gmail.com'
ppat = '[+](0|91)?[-\s]?[6-9][0-9]{9}'
phone = input('enter valid phone numbers with code :- ')
# phone = '+91-7047257520'
npat = '[A-Z][a-z]{1,20}?[\s]?[A-Z][a-z]{1,20}'
name = input('enter valid name with last name in capitalize :- ')
# name = 'Vidhan Sharma'

fm = re.fullmatch(ppat, phone)
m = re.match(npat, name)
em = re.match(epat, email)

if em != None:
    if fm != None:
        if m != None:
            print('successfully enter')
        else:
            print('name pattern doesnt match first letter of name and last name should be capital')
    else:
        print('phone pattern doesnt match first add + and 0/91 then write numbers with space or -')
else:
    print('email pattern doesnt match')