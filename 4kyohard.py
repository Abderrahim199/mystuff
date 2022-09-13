# here, i'm going to do that kata:

def numbers_sumUp_to_a_number(n,listo=[]):
    the_n = n**2
    if the_n == 0:
        return listo
    
    elif the_n -(n-1)**2 >1 and 1 not in listo:
        listo.append(n-1)
        the_n = the_n - (n-1)**2
    elif the_n >=1 and 1  in listo:
        the_n += (listo.pop())**2
        number = listo.pop()
        the_n += (number)**2
        the_n = the_n - (number -1)**2
    else:
        return numbers_sumUp_to_a_number(the_n,listo)



print(numbers_sumUp_to_a_number(10))

        

