# mod ---> teacher ---> python module

from student.cs import cs_fun
cs_fun()

# import sys
# sys.path.append('D:/python/Modules/mod/student')
# import cs
# cs.cs_fun()

# (python -m teacher.fun) this command is used to run globally this fun and our directory should look like (PS D:\python\Modules\mod>)

def python_fun():
    print('mod ---> teacher ---> python fun')