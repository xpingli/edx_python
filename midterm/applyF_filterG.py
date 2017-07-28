def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    # Your code here
    
    assert type(L) == list
    
    L_copy = L[::]
    
    for i in L_copy:
        if g(f(i)) == False:
            L.remove(i)

    if len(L) == 0:
        return -1

    return max(L)
    
            

            