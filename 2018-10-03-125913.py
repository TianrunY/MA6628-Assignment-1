# MA 6628 Assignment 1
# Tianrun Yu

import math
import sys
def isprime (n):
    if n <= 1:
        return 0
    if n%2 == 0:
        return 0
    for x in range(3,int(n**0.5)+1,2):
        if n%x == 0:
            return 0
    return 1
if __name__ == "__main__":
    a,b=1000,1002
    count =0
    for x in range(1000,1000000):
        if isprime(x)*isprime(x+2):
            a,b=x,x+2
            count = count +1
    print('The total number of twin primes between one thousand and one million is %d' %count)
    print('The biggest twin prime is %d %d' %(a,b))
