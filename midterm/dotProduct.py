def dotProduct(listA, listB):
    """
    listA: a list of numbers
    listB: a list of numbers same length of A
    """
    
    #try:
        
        #if len(listA) != len(listB):
            #raise ValueError('listA and listB should be same length')
        
    #except ValueError as msg:
        
        #return msg
    
    
    # use assert this time
    assert len(listA) == len(listB), 'The length of A and B should be equal'
    
    product = sum([z1*z2 for z1, z2 in zip(listA, listB)])
    
    return product
        
        
