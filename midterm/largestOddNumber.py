def largest_odd_times(L):
    """
    Assume L is a non empty list of ints
    
    Returns the largest element of L that occurs an odd number of times in L.
    If no such element exists, returns None.
    """
    

    convert2string = str(L)
    
    try:
        largest = None
        for i in L:
        
            n = convert2string.count(str(i))
        
            if n % 2 != 0:
              
                if largest is None or i > largest:
                
                    largest = i
                
        return largest
    except:
        print('L contains only integers as its elements')

