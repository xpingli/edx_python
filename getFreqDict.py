def getFreqDict(string):
    """
    string: a string of letters as input.
    
    returns a dictionary with the frequency of each letter.
    """
    
    d = {}
    for i in string:
        i = i.lower()
        d[i] = d.get(i, 0) + 1
        
    return d