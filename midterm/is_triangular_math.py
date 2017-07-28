def is_triangular_math(k):
    """
    a new version applying math formular to determine if k is a triangular number.
    
    k = n(n+1)/2
    
    returns a boolean
    """
    
    k = int(k)
    
    if k == 0:
        return 0
    
    elif k > 0:
        
        for i in range(k):
            i = i + 1
            
            if 2*k == i*(i + 1):
                return True, i
            
        return False
