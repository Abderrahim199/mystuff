
# let's start
import threading
import time
then = time.time()

print('Start of program.')



def takeANap():
    time.sleep(5)
    print('Wake Up!')

threadObj = threading.Thread(target = takeANap)
threadObj.start()


print('End of program.')

now = time.time()
print(' this is the difference %s !.' % (now - then))
# the end of this program

