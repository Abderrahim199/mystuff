# let's write the sorting algorithm here.

def sorting(array):
    if len(array) <= 1:
        return array
    else:
        pivot = (len(array))//2
        return sorting([element for element in array if element < array[pivot]]) + [array[pivot]] + sorting([element for element in array if element > array[pivot]])


print(sorting([1,1,1,1]))



print(sorting([5,10,9,0,1,3,19]))

