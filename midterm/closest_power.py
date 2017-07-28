def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # base > 1
    # integer > 0    
    n = int(base)
    num = int(num)
    r = num // n # r - exponent
    
    if n <=1 or num <= 0:
        return 'base > 1 and num > 0'
    
    smallest_diff = None
    basket = []
    for i in range(r + 1):
        
        ds = abs(n**i - num)
        
        if smallest_diff is None or ds < smallest_diff:
           
            smallest_diff = ds
            
            basket.append((smallest_diff, i))
            
    basket.sort()
        
            
    return basket[0][1]
        
        
        
        
print(closest_power(5, 12))
        
        
    
    
    
    
    