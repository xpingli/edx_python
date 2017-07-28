def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    if len(L1) != len(L2):
        return False
    
    d1 = {}
    for i in L1:
        d1[i] = d1.get(i, 0) + 1
        
    d2 = {}
    for i in L2:
        d2[i] = d2.get(i, 0) + 1
        
        
    if d1.keys() != d2.keys():
        return False
    
    new_d = {}
    for key, value in d1.items():
        
        new_d[value] = key
        

    sorted_new_d = sorted(new_d, reverse = True)

    return (sorted_new_d[0], new_d[sorted_new_d[0]], type(new_d[sorted_new_d[0]]))
        

    
    