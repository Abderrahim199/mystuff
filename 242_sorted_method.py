def insertion_sort_for(a):
    for i in range(1, len(a)):
        for j in range(i-1, -1, -1):
            if a[j+1] < a[j]:
                a[j], a[j+1] = a[j+1], a[j]
            else:
                break
    return a


tests = [[1,5,2,6,-1,0],[4,2,5,0]]
for test in tests:
    print(insertion_sort_for(test))


