
def gcd(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    while True:
        if a<0 or b<0:
            print "ValueError"
            break
        elif ((type(a)!=int or type(a)!=int) or (type(b)!=int or type(a)!=int)):
            print "TypeError"
            break
        else:
            i=max(a,b)
            if b%a==0 or a%b==0:
                return a
            else:
                while i>=1:
                    if b%i==0 and a%i==0:
                        return i
                        break
                    i-=1               