# i will calculate if you have a 50000 dh or any money, how much we gonna end up having after 20 years 
#if the return is 30% of the money we put each year!
import time
def how_much_is_the_return(how_much_we_put):
    year = 1
    while year <=20:
        year +=1
        how_much_we_put += 0.3*how_much_we_put
        time.sleep(2)
        print('this is how much money we have %s in million %s million  in the %s year a3mi! haha' % (how_much_we_put, how_much_we_put/10000, year))

    return ' '

money = int(input('how much money you wanna put?: '))

print(how_much_is_the_return(money))
# we are done!


