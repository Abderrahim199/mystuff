# that's it!
# let's start.
import datetime,time
halloween2021 = datetime.datetime(2021,10,31,0,0,0)
then = time.time()
while datetime.datetime.now() < halloween2021:
    time.sleep(1)
    print('it\'s not yeeet!')
    now = time.time()
    dif = now - then
    then = now
    print('this is how much my pc is low: %s' % (dif))

# Done!.

