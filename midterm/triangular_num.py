def is_triangular(k):
    """
    k: a positive integer
    returns a boolen. True for is triangular False for not.
    
    A triangular number is continued summation of integers: 1+2 =3, 1+2+3 = 6 
    """
    try:
        k = int(k)
    except TypeError:
        return 'k is a positive integer'
    
    
    if k == 0:
        return 0
    
    
    total = 0
    n = 0
    
    while total < k:
        
        n += 1
        
        total += n 
        
        if total == k:
            
            return True
        
        
    return False

