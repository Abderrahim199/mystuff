

def is_valid_IP(strng):
    
    try:         
        
        string = '.'.join([str(int(element)) for element in strng.split('.')])
        
        return strng == string and len([element for element in strng.split('.') if int(element) >= 0 and int(element) <= 255]) == 4     
    except:
        return False



import re
def is_valid_IP(strng):
    return bool(re.match(r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])(\.(?!$)|$)){4}(?=$)',strng))



def is_valid_IP(s):
    return s.count('.')==3 and all(o.isdigit() and 0<=int(o)<=255 and str(int(o))==o for o in s.split('.'))

