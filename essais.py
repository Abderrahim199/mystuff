from random import *

def essays(essay=0):
    d = randint(1,6)
    print(d)
    if d== 6:
        return 0
    else:
        return 1 + essays()


print('this is how many essays ', essays() )
