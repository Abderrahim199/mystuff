import time
# first problem.

def sumoftwo(List,target):
    for element in List:
        if (target-element) in List:
            
            return [List.index(element),List.index(target-element)]
    return []
then = time.time()
print("abdelkrim rajel mezian")
print(sumoftwo([2,7,11,15], 9))
now = time.time()
print('this is the time: ', now - then)

