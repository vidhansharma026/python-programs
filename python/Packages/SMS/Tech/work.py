# SMS ---> Tech ---> work file or module

# siblings import

#  we want to use user module in tech module

# from User import request
# request.user_request()

from User.reqst import user_request
user_request()

# orrr

# import sys
# sys.path.append('D:/python/Packages/SMS/User')
# import reqst

# reqst.user_request()
# siblings import

def tech_work():
    print('SMS ---> Tech ---> work file or module')
    print('tech_work function')
    print()
    user_request()
