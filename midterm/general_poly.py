def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 
    
    for example: general_poly([1, 2, 3, 4])(10)
    
    """
    L_copy = L[::]
   
    def x_value(x):
        
        rev_list = list(range(len(L_copy)))
        rev_list.reverse()

        total = 0
        for i in range(len(L_copy)):
            total += L[i] * (x ** rev_list[i])
        return total
    
    return x_value # return a function
        



        