# here, i'm going to solve the given problem! god willing.
import time
def searchAnumber(listi,number):
    if number in listi:
        low = 0
        high = len(listi)-1
        mid = (low+high)//2
        while listi[mid] != number:
            if listi[mid]>number:
                mid = mid -1
            else:
                mid +=1
        return mid
    else:
        return 'number not in the list!'



listo = [13,11,10,7,4,3,1,0]
number = 7
then = time.time()
print(searchAnumber(listi,number))
now = time.time()
