# -*- coding: utf-8 -*-
'''
This is a test written for gcd function
'''

from gcd import gcd

def test_gcd():
    try: 
        assert gcd(48, 64) == 16
        assert gcd(44, 19) == 1
        print "test successful"
    except AssertionError: 
        print "Assertion error for gcd"
        #assert gcd(-1, -1) == -1
    except TypeError:
        print "Type Error"
            
    
if __name__ =='__main__':
    test_gcd()