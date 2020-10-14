#efficient algorithm for combinations and permutions

#note: it based on math library
#from math library it use factorial
import math

def combinations(n, r):
    
    r,s = max(n-r, r),min(n-r, r)
    com = n
    for i in range(n-1, r, -1):
        com *=i
    com //= math.factorial(s)
    
    return com



