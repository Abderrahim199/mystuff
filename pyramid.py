def cube(n=8):
    print('*'*8)
    for i in range(1,n//2):
        print('*' +' '*i + '*' + ' '*(n-2*i) + '*' + ' '*i + '*')
        return ' '

print(cube())

