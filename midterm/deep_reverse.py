def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    # Your code here
    
    assert type(L) == list, 'L must be a list'
    
    L.reverse()
    
    [i.reverse() for i in L]
    
