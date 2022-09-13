def etoile(n):
    i,k =1,1
    while i<=n:
        
        print(('*'*k).center(2*2*n))
        k+=2
        i+=1
    return ''




print(etoile(7))

